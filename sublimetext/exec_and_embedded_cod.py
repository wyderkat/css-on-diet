import sublime, sublime_plugin
import os, sys
import threading
import subprocess
import functools
import time
import imp

PACKAGeDIR = "CSS-On-Diet"

# "_COMMENT ON MS WINDOWS": "embedded COD works in Windows, but it excludes using external COD preprocessor. If shell is True, we cannot catch exception if external command is missing, and we cannot run embedded version then"


class ProcessListener(object):
    def on_data(self, proc, data):
        pass

    def on_finished(self, proc):
        pass

# Run included COD preprocessor as a Python module
# in a separate thread, forwarding stdout to a supplied
# ProcessListener (on that thread)
class EmbeddedCODInThread(threading.Thread):
  def __init__(me, cmd, env, listener, path="", shell=False):

    threading.Thread.__init__(me, name="cssondiet")
    me.finished = False
    me.exitcode = 0
    me.listener = listener

    output = None
    try:
      idx = cmd.index("-o")
      output = cmd[idx+1]
    except:
      output = False

    minify = "-m" in cmd

    inputfile = cmd[-1]
    if output == False or output == inputfile:
      output = inputfile+".css"

    class an_argument(object):
      def __init__(me, input, output="-", minify=False ):
        me.cod_files = [ input ]
        me.output = output
        me.no_comments = False
        me.no_header = False
        me.minify_css = minify
    me.args = an_argument( inputfile, output, minify )

    print("Actually running embedded COD script with inputfile=%s, " \
        "output=%s, minify=%s\n" %( inputfile, output, str(minify)) )
    script_dir = os.path.join( sublime.packages_path(), PACKAGeDIR )
    #me.read_stderr("script_dir: %s\n" % script_dir )

    me.start_time = time.time()

    try:
      fp, pathname, description = imp.find_module("cod", [script_dir])
      try:
        me.cod_module = imp.load_module("cod", fp, pathname, description)
      finally:
        if fp:
          fp.close()
    except ImportError:
      me.read_stderr("[Error loading embedded COD preprocessor]\n")
      me.finished = True
      if me.listener:
        me.listener.on_finished(me)
      return

    me.start()

  def run(me):

    try:
      me.exitcode = me.cod_module.put_css_on_diet( me.args, me.read_stderr )
    except me.cod_module.a_preprocess_error as e:
      me.read_stderr("[Preprocessing Error No. %d]\n" % e.errorcode)
    except Exception as e:
      me.read_stderr("[Internal error of COD preprocessor: %s]\n" % str(e))
    finally:
      me.finished = True
      if me.listener:
        me.listener.on_finished(me)

  def kill(me):
    pass # TODO in COD
    #if not me.killed:
    #  me.killed = True
    #  me.listener = None

  def poll(me):
    # TODO lock
    return not me.finished

  def exit_code(me):
    # TODO lock
    return me.exitcode

  def read_stderr(me, data):
    if me.listener:
      me.listener.on_data(me, data, pythonstring=True)



if sublime.version()[0] == "2":


    class ExecAndEmbeddedCodCommand(sublime_plugin.WindowCommand, ProcessListener):
        def run(self, cmd = [], file_regex = "", line_regex = "", working_dir = "",
                encoding = "utf-8", env = {}, quiet = False, kill = False,
                # Catches "path" and "shell"
                **kwargs):

            if kill:
                if self.proc:
                    self.proc.kill()
                    self.proc = None
                    self.append_data(None, "[Cancelled]")
                return

            if not hasattr(self, 'output_view'):
                # Try not to call get_output_panel until the regexes are assigned
                self.output_view = self.window.get_output_panel("exec")

            # Default the to the current files directory if no working directory was given
            if (working_dir == "" and self.window.active_view()
                            and self.window.active_view().file_name()):
                working_dir = os.path.dirname(self.window.active_view().file_name())

            self.output_view.settings().set("result_file_regex", file_regex)
            self.output_view.settings().set("result_line_regex", line_regex)
            self.output_view.settings().set("result_base_dir", working_dir)

            # Call get_output_panel a second time after assigning the above
            # settings, so that it'll be picked up as a result buffer
            self.window.get_output_panel("exec")

            self.encoding = encoding
            self.quiet = quiet

            self.proc = None
            if not self.quiet:
                print ("Running " + " ".join(cmd))
                sublime.status_message("Building")

            show_panel_on_build = sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build", True)
            if show_panel_on_build:
                self.window.run_command("show_panel", {"panel": "output.exec"})

            merged_env = env.copy()
            if self.window.active_view():
                user_env = self.window.active_view().settings().get('build_env')
                if user_env:
                    merged_env.update(user_env)

            # Change to the working dir, rather than spawning the process with it,
            # so that emitted working dir relative path names make sense
            if working_dir != "":
                os.chdir(working_dir)

            err_type = OSError
            if os.name == "nt":
                err_type = WindowsError

            try:
                # Forward kwargs to AsyncProcess
                self.proc = AsyncProcess(cmd, merged_env, self, **kwargs)
            except err_type as e:
                if e.errno != 2: # no such file
                  self.append_data(None, str(e) + "\n")
                  self.append_data(None, "[cmd:  " + str(cmd) + "]\n")
                  self.append_data(None, "[dir:  " + str(os.getcwdu()) + "]\n")
                  if "PATH" in merged_env:
                      self.append_data(None, "[path: " + str(merged_env["PATH"]) + "]\n")
                  else:
                      self.append_data(None, "[path: " + str(os.environ["PATH"]) + "]\n")
                  if not self.quiet:
                      self.append_data(None, "[Failed]")
                else:
                  try:
                    self.proc = EmbeddedCODInThread(cmd, merged_env, self, **kwargs)
                  except Exception as ee:
                    self.append_data(None, 
                      "Exception from embedded COD preprocessor: %s \n" % str(ee) )
                    if not self.quiet:
                        self.append_data(None, "[Failed]")

        def is_enabled(self, kill = False):
            if kill:
                return hasattr(self, 'proc') and self.proc and self.proc.poll()
            else:
                return True

        def append_data(self, proc, data):
            if proc != self.proc:
                # a second call to exec has been made before the first one
                # finished, ignore it instead of intermingling the output.
                if proc:
                    proc.kill()
                return

            try:
                str = data.decode(self.encoding)
            except:
                str = "[Decode error - output not " + self.encoding + "]\n"
                proc = None

            # Normalize newlines, Sublime Text always uses a single \n separator
            # in memory.
            str = str.replace('\r\n', '\n').replace('\r', '\n')

            selection_was_at_end = (len(self.output_view.sel()) == 1
                and self.output_view.sel()[0]
                    == sublime.Region(self.output_view.size()))
            self.output_view.set_read_only(False)
            edit = self.output_view.begin_edit()
            self.output_view.insert(edit, self.output_view.size(), str)
            if selection_was_at_end:
                self.output_view.show(self.output_view.size())
            self.output_view.end_edit(edit)
            self.output_view.set_read_only(True)

        def finish(self, proc):
            if not self.quiet:
                elapsed = time.time() - proc.start_time
                exit_code = proc.exit_code()
                if exit_code == 0 or exit_code == None:
                    self.append_data(proc, ("[Finished in %.1fs]") % (elapsed))
                else:
                    self.append_data(proc, ("[Finished in %.1fs with exit code %d]") % (elapsed, exit_code))

            if proc != self.proc:
                return

            errs = self.output_view.find_all_results()
            if len(errs) == 0:
                sublime.status_message("Build finished")
            else:
                sublime.status_message(("Build finished with %d errors") % len(errs))

            # Set the selection to the start, so that next_result will work as expected
            edit = self.output_view.begin_edit()
            self.output_view.sel().clear()
            self.output_view.sel().add(sublime.Region(0))
            self.output_view.end_edit(edit)

        def on_data(self, proc, data, pythonstring = False):
            sublime.set_timeout(functools.partial(self.append_data, proc, data), 0)

        def on_finished(self, proc):
            sublime.set_timeout(functools.partial(self.finish, proc), 0)


    # Encapsulates subprocess.Popen, forwarding stdout to a supplied
    # ProcessListener (on a separate thread)
    class AsyncProcess(object):
        def __init__(self, arg_list, env, listener,
                # "path" is an option in build systems
                path="",
                # "shell" is an options in build systems
                shell=False):
    
            self.listener = listener
            self.killed = False
    
            self.start_time = time.time()
    
            # Hide the console window on Windows
            startupinfo = None
            if os.name == "nt":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    
            # Set temporary PATH to locate executable in arg_list
            if path:
                old_path = os.environ["PATH"]
                # The user decides in the build system whether he wants to append $PATH
                # or tuck it at the front: "$PATH;C:\\new\\path", "C:\\new\\path;$PATH"
                os.environ["PATH"] = os.path.expandvars(path).encode(sys.getfilesystemencoding())
    
            proc_env = os.environ.copy()
            proc_env.update(env)
            for k, v in proc_env.iteritems():
                proc_env[k] = os.path.expandvars(v).encode(sys.getfilesystemencoding())
    
            self.proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, startupinfo=startupinfo, env=proc_env, shell=shell)
    
            if path:
                os.environ["PATH"] = old_path
    
            if self.proc.stdout:
                threading.Thread(target=self.read_stdout).start()
    
            if self.proc.stderr:
                threading.Thread(target=self.read_stderr).start()
    
        def kill(self):
            if not self.killed:
                self.killed = True
                self.proc.terminate()
                self.listener = None
    
        def poll(self):
            return self.proc.poll() == None
    
        def exit_code(self):
            return self.proc.poll()
    
        def read_stdout(self):
            while True:
                data = os.read(self.proc.stdout.fileno(), 2**15)
    
                if data != "":
                    if self.listener:
                        self.listener.on_data(self, data)
                else:
                    self.proc.stdout.close()
                    if self.listener:
                        self.listener.on_finished(self)
                    break
    
        def read_stderr(self):
            while True:
                data = os.read(self.proc.stderr.fileno(), 2**15)
    
                if data != "":
                    if self.listener:
                        self.listener.on_data(self, data)
                else:
                    self.proc.stderr.close()
                    break


elif sublime.version()[0] == "3":


    class ExecAndEmbeddedCodCommand(sublime_plugin.WindowCommand, ProcessListener):
        def run(self, cmd = None, shell_cmd = None, file_regex = "", line_regex = "", working_dir = "",
                encoding = "utf-8", env = {}, quiet = False, kill = False,
                word_wrap = True, syntax = "Packages/Text/Plain text.tmLanguage",
                # Catches "path" and "shell"
                **kwargs):

            if kill:
                if self.proc:
                    self.proc.kill()
                    self.proc = None
                    self.append_string(None, "[Cancelled]")
                return

            if not hasattr(self, 'output_view'):
                # Try not to call get_output_panel until the regexes are assigned
                self.output_view = self.window.create_output_panel("exec")

            # Default the to the current files directory if no working directory was given
            if (working_dir == "" and self.window.active_view()
                            and self.window.active_view().file_name()):
                working_dir = os.path.dirname(self.window.active_view().file_name())

            self.output_view.settings().set("result_file_regex", file_regex)
            self.output_view.settings().set("result_line_regex", line_regex)
            self.output_view.settings().set("result_base_dir", working_dir)
            self.output_view.settings().set("word_wrap", word_wrap)
            self.output_view.settings().set("line_numbers", False)
            self.output_view.settings().set("gutter", False)
            self.output_view.settings().set("scroll_past_end", False)
            self.output_view.assign_syntax(syntax)

            # Call create_output_panel a second time after assigning the above
            # settings, so that it'll be picked up as a result buffer
            self.window.create_output_panel("exec")

            self.encoding = encoding
            self.quiet = quiet

            self.proc = None
            if not self.quiet:
                if shell_cmd:
                    print("Running " + shell_cmd)
                else:
                    print("Running " + " ".join(cmd))
                sublime.status_message("Building")

            show_panel_on_build = sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build", True)
            if show_panel_on_build:
                self.window.run_command("show_panel", {"panel": "output.exec"})

            merged_env = env.copy()
            if self.window.active_view():
                user_env = self.window.active_view().settings().get('build_env')
                if user_env:
                    merged_env.update(user_env)

            # Change to the working dir, rather than spawning the process with it,
            # so that emitted working dir relative path names make sense
            if working_dir != "":
                os.chdir(working_dir)

            self.debug_text = ""
            if shell_cmd:
                self.debug_text += "[shell_cmd: " + shell_cmd + "]\n"
            else:
                self.debug_text += "[cmd: " + str(cmd) + "]\n"
            self.debug_text += "[dir: " + str(os.getcwd()) + "]\n"
            if "PATH" in merged_env:
                self.debug_text += "[path: " + str(merged_env["PATH"]) + "]"
            else:
                self.debug_text += "[path: " + str(os.environ["PATH"]) + "]"

            try:
                # Forward kwargs to AsyncProcess
                self.proc = AsyncProcess(cmd, shell_cmd, merged_env, self, **kwargs)
            except Exception as e:
                if e.errno != 2: # no such file
                  self.append_string(None, str(e) + "\n")
                  self.append_string(None, self.debug_text + "\n")
                  if not self.quiet:
                      self.append_string(None, "[Failed]")
                else:
                  try:
                    self.proc = EmbeddedCODInThread(cmd, merged_env, self, **kwargs)
                  except Exception as ee:
                    self.append_string(None, 
                      "Exception from embedded COD preprocessor: %s \n" % str(ee) )
                    if not self.quiet:
                        self.append_string(None, "[Failed]")

        def is_enabled(self, kill = False):
            if kill:
                return hasattr(self, 'proc') and self.proc and self.proc.poll()
            else:
                return True

        def append_data(self, proc, data):
            if proc != self.proc:
                # a second call to exec has been made before the first one
                # finished, ignore it instead of intermingling the output.
                if proc:
                    proc.kill()
                return

            try:
                str = data.decode(self.encoding)
            except:
                str = "[Decode error - output not " + self.encoding + "]\n"
                proc = None

            # Normalize newlines, Sublime Text always uses a single \n separator
            # in memory.
            str = str.replace('\r\n', '\n').replace('\r', '\n')

            self.output_view.run_command('append', {'characters': str, 'force': True, 'scroll_to_end': True})

        def append_string(self, proc, str):
            self.append_data(proc, str.encode(self.encoding))

        def finish(self, proc):
            if not self.quiet:
                elapsed = time.time() - proc.start_time
                exit_code = proc.exit_code()
                if exit_code == 0 or exit_code == None:
                    self.append_string(proc,
                        ("[Finished in %.1fs]" % (elapsed)))
                else:
                    self.append_string(proc, ("[Finished in %.1fs with exit code %d]\n"
                        % (elapsed, exit_code)))
                    self.append_string(proc, self.debug_text)

            if proc != self.proc:
                return

            errs = self.output_view.find_all_results()
            if len(errs) == 0:
                sublime.status_message("Build finished")
            else:
                sublime.status_message(("Build finished with %d errors") % len(errs))

        def on_data(self, proc, data, pythonstring = False):
          if pythonstring:
            sublime.set_timeout(functools.partial(self.append_string, proc, data), 0)
          else:
            sublime.set_timeout(functools.partial(self.append_data, proc, data), 0)

        def on_finished(self, proc):
            sublime.set_timeout(functools.partial(self.finish, proc), 0)

    # Encapsulates subprocess.Popen, forwarding stdout to a supplied
    # ProcessListener (on a separate thread)
    class AsyncProcess(object):
        def __init__(self, cmd, shell_cmd, env, listener,
                # "path" is an option in build systems
                path="",
                # "shell" is an options in build systems
                shell=False):
    
            if not shell_cmd and not cmd:
                raise ValueError("shell_cmd or cmd is required")
    
            if shell_cmd and not isinstance(shell_cmd, str):
                raise ValueError("shell_cmd must be a string")
    
            self.listener = listener
            self.killed = False
    
            self.start_time = time.time()
    
            # Hide the console window on Windows
            startupinfo = None
            if os.name == "nt":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    
            # Set temporary PATH to locate executable in cmd
            if path:
                old_path = os.environ["PATH"]
                # The user decides in the build system whether he wants to append $PATH
                # or tuck it at the front: "$PATH;C:\\new\\path", "C:\\new\\path;$PATH"
                os.environ["PATH"] = os.path.expandvars(path)
    
            proc_env = os.environ.copy()
            proc_env.update(env)
            for k, v in proc_env.items():
                proc_env[k] = os.path.expandvars(v)
    
            if shell_cmd and sys.platform == "win32":
                # Use shell=True on Windows, so shell_cmd is passed through with the correct escaping
                self.proc = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, startupinfo=startupinfo, env=proc_env, shell=True)
            elif shell_cmd and sys.platform == "darwin":
                # Use a login shell on OSX, otherwise the users expected env vars won't be setup
                self.proc = subprocess.Popen(["/bin/bash", "-l", "-c", shell_cmd], stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, startupinfo=startupinfo, env=proc_env, shell=False)
            elif shell_cmd and sys.platform == "linux":
                # Explicitly use /bin/bash on Linux, to keep Linux and OSX as
                # similar as possible. A login shell is explicitly not used for
                # linux, as it's not required
                self.proc = subprocess.Popen(["/bin/bash", "-c", shell_cmd], stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, startupinfo=startupinfo, env=proc_env, shell=False)
            else:
                # Old style build system, just do what it asks
                self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, startupinfo=startupinfo, env=proc_env, shell=shell)
    
            if path:
                os.environ["PATH"] = old_path
    
            if self.proc.stdout:
                threading.Thread(target=self.read_stdout).start()
    
            if self.proc.stderr:
                threading.Thread(target=self.read_stderr).start()
    
        def kill(self):
            if not self.killed:
                self.killed = True
                if sys.platform == "win32":
                    # terminate would not kill process opened by the shell cmd.exe, it will only kill
                    # cmd.exe leaving the child running
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    subprocess.Popen("taskkill /PID " + str(self.proc.pid), startupinfo=startupinfo)
                else:
                    self.proc.terminate()
                self.listener = None
    
        def poll(self):
            return self.proc.poll() == None
    
        def exit_code(self):
            return self.proc.poll()
    
        def read_stdout(self):
            while True:
                data = os.read(self.proc.stdout.fileno(), 2**15)
    
                if len(data) > 0:
                    if self.listener:
                        self.listener.on_data(self, data)
                else:
                    self.proc.stdout.close()
                    if self.listener:
                        self.listener.on_finished(self)
                    break
    
        def read_stderr(self):
            while True:
                data = os.read(self.proc.stderr.fileno(), 2**15)
    
                if len(data) > 0:
                    if self.listener:
                        self.listener.on_data(self, data)
                else:
                    self.proc.stderr.close()
                    break
    
    
    
    
