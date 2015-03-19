#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Copyright 2014-2015 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##

##
# Coding Standard:
# No PEP8 compatibility! Especially:
# - Indentation is just 2 spaces
# - The word "me" is used instead of "self" 
# - Extra spaces are used in parentheses to increase readability

#{{{ import

from __future__ import division  # Compatibility

import hashlib
import math
import re
import sys
import time
from os import path

#}}}


""" CSS-On-Diet is an easy and fast CSS preprocessor for CSS files. """


VERSION = "1.8"
PROToVERSION = "1.8"

#{{{ Prefixes List

# !!! don't forget the period character when a single element in a tuple
PREFIXES = {
  # http://www.w3schools.com/cssref/css3_browsersupport.asp
  "align-content": ("-webkit-",), 
  "align-items": ("-webkit-",), 
  "align-self": ("-webkit-",), 
  "animation": ("-webkit-",), 
  "animation-name": ("-webkit-",), 
  "animation-duration": ("-webkit-",), 
  "animation-timing-function": ("-webkit-",), 
  "animation-delay": ("-webkit-",), 
  "animation-iteration-count": ("-webkit-",), 
  "animation-direction": ("-webkit-",), 
  "animation-play-state": ("-webkit-",), 
  "backface-visibility": ("-webkit-","-ms-"), 
  "column-count": ("-webkit-", "-moz-",),
  "column-fill": ("-webkit-", "-moz-",),
  "column-gap": ("-webkit-", "-moz-",),
  "column-rule": ("-webkit-", "-moz-",),
  "column-rule-color": ("-webkit-", "-moz-",),
  "column-rule-style": ("-webkit-", "-moz-",),
  "column-rule-width": ("-webkit-", "-moz-",),
  "column-span": ("-webkit-", "-moz-",),
  "column-width": ("-webkit-", "-moz-",),
  "columns": ("-webkit-", "-moz-",),
  "flex": ("-webkit-","-ms-"),
  "flex-basis": ("-webkit-",),
  "flex-direction": ("-webkit-",),
  "flex-flow": ("-webkit-",),
  "flex-grow": ("-webkit-",),
  "flex-shrink": ("-webkit-",),
  "flex-wrap": ("-webkit-",),
  "font-feature-setting": ("-webkit-", "-moz-",),
  "hyphens": ("-webkit-", "-moz-", "-ms-",),
  "image-rendering": ("-moz-",),
  "justify-content" : ("-webkit-",),
  "marquee-direction": ("-webkit-",),
  "marquee-play-count": ("-webkit-",),
  "marquee-speed": ("-webkit-",),
  "marquee-style": ("-webkit-",),
  "order": ("-webkit-","-ms-flex-"), # not typical
  "perspective": ("-webkit-",),
  "perspective-origin": ("-webkit-",),
  "tab-size": ("-moz-",),
  "text-align-last": ("-moz-",),
  "text-decoration-color": ("-moz-",),
  "text-decoration-line": ("-moz-",),
  "text-decoration-style": ("-moz-",),
  "transform": ("-webkit-",),
  "transform-origin": ("-webkit-",),
  "transform-style": ("-webkit-",),
}

ATRULESPREFIXES = {
  "keyframes": ("-webkit-",)
}

#}}}
#{{{ Mnemonics List

PROPERTyMNEMONICS = {
  "col":"color",
  "wid":"width",
  "hei":"height",
  "bac":"background-color",
  "bai":"background-image",
  "bap":"background-position",
  "ba-":"background",
  "bas":"background-size",
  "bar":"background-repeat",
  "bal":"background-clip",
  "bao":"background-origin",
  "dis":"display",
  "con":"content",
  "fos":"font-size",
  "fow":"font-weight",
  "fof":"font-family",
  "fot":"font-style",
  "fo-":"font",
  "fov":"font-variant",
  "pos":"position",
  "pa-":"padding",
  "pal":"padding-left",
  "pat":"padding-top",
  "pab":"padding-bottom",
  "par":"padding-right",
  "ma-":"margin",
  "mal":"margin-left",
  "mat":"margin-top",
  "mab":"margin-bottom",
  "mar":"margin-right",
  "flo":"float",
  "top":"top",
  "lih":"line-height",
  "fl-":"flex",
  "flf":"flex-flow",
  "fld":"flex-direction",
  "flw":"flex-wrap",
  "flg":"flex-grow",
  "fls":"flex-shrink",
  "flb":"flex-basis",
  "ord":"order",
  "als":"align-self",
  "ali":"align-items",
  "alc":"align-content",
  "juc":"justify-content",
  "b--":"border",
  "bb-":"border-bottom",
  "bbc":"border-bottom-color",
  "bbl":"border-bottom-left-radius",
  "bbr":"border-bottom-right-radius",
  "bbs":"border-bottom-style",
  "bbw":"border-bottom-width",
  "bcp":"border-collapse",
  "bco":"border-color",
  "bi-":"border-image",
  "bio":"border-image-outset",
  "bir":"border-image-repeat",
  "bil":"border-image-slice",
  "bis":"border-image-source",
  "biw":"border-image-width",
  "bl-":"border-left",
  "blc":"border-left-color",
  "bls":"border-left-style",
  "blw":"border-left-width",
  "bra":"border-radius",
  "br-":"border-right",
  "brc":"border-right-color",
  "brs":"border-right-style",
  "brw":"border-right-width",
  "bsp":"border-spacing",
  "bst":"border-style",
  "bt-":"border-top",
  "btc":"border-top-color",
  "btl":"border-top-left-radius",
  "btr":"border-top-right-radius",
  "bts":"border-top-style",
  "btw":"border-top-width",
  "bwi":"border-width",
  "lef":"left",
  "tea":"text-align",
  "ted":"text-decoration",
  "tet":"text-transform",
  "tes":"text-shadow",
  "tei":"text-indent",
  "teo":"text-overflow",
  "ter":"text-rendering",
  "zin":"z-index",
  "vea":"vertical-align",
  "ov-":"overflow",
  "ovx":"overflow-x",
  "ovy":"overflow-y",
  "opa":"opacity",
  "cle":"clear",
  "les":"letter-spacing",
  "cur":"cursor",
  "rig":"right",
  "ouc":"outline-color",
  "ou-":"outline",
  "ous":"outline-style",
  "ouo":"outline-offset",
  "ouw":"outline-width",
  "bot":"bottom",
  "li-":"list-style",
  "lit":"list-style-type",
  "lii":"list-style-image",
  "lio":"list-style-position",
  "bos":"box-shadow",
  "boz":"box-sizing",
  "zoo":"zoom",
  "maw":"max-width",
  "miw":"min-width",
  "mih":"min-height",
  "mah":"max-height",
  "fil":"filter",
  "whs":"white-space",
  "vis":"visibility",
  "wos":"word-spacing",
  "wob":"word-break",
  "wow":"word-wrap",
  "an-":"animation",
  "ann":"animation-name",
  "and":"animation-duration",
  "ant":"animation-timing-function",
  "any":"animation-delay",
  "ani":"animation-iteration-count",
  "anr":"animation-direction",
  "anf":"animation-fill-mode",
  "anp":"animation-play-state",
  "tf-":"transform",
  "tfo":"transform-origin",
  "tfs":"transform-style",
  "ti-":"transition",
  "tiy":"transition-delay",
  "tid":"transition-duration",
  "tip":"transition-property",
  "tit":"transition-timing-function",
  # another variant
  "ts-":"transition",
  "tsy":"transition-delay",
  "tsd":"transition-duration",
  "tsp":"transition-property",
  "tst":"transition-timing-function",
}

VALUeMNEMONICS = {
  "!i":"!important",
  "%%":"100%",
  "ab":"absolute",
  "al":"all",
  "au":"auto",
  "ba":"baseline",
  "bb":"border-box",
  "bh":"both",
  "bl":"block",
  "bo":"bold",
  "bt":"bottom",
  "ca":"capitalize",
  "cb":"content-box",
  "ce":"center",
  "co":"column",
  "da":"dashed",
  "db":"double",
  "de":"default",
  "do":"dotted",
  "ea":"ease",
  "ei":"ease-in",
  "eo":"ease-out",
  "fi":"fixed",
  "fl":"flex",
  "fs":"flex-start",
  "fe":"flex-end",
  "hi":"hidden",
  "ib":"inline-block",
  "if":"infinite",
  "ih":"inherit",
  "ii":"initial",
  "il":"inline",
  "io":"ease-in-out",
  "is":"inset",
  "it":"italic",
  "le":"left",
  "lg":"linear-gradient",
  "li":"linear",
  "lo":"lowercase",
  "mi":"middle",
  "nm":"normal",
  "no":"none",
  "nr":"no-repeat",
  "nw":"nowrap",
  "pb":"padding-box",
  "po":"pointer",
  "re":"relative",
  "rg":"radial-gradient",
  "ri":"right",
  "ro":"row",
  "rx":"repeat-x",
  "ry":"repeat-y",
  "sa":"space-around",
  "sb":"space-between",
  "sc":"stretch",
  "so":"solid",
  "st":"static",
  "ta":"table",
  "to":"top",
  "tr":"transparent",
  "un":"underline",
  "up":"uppercase",
  "vi":"visible",
  "wh":"white",
  "wr":"wrap",
}

UNItMNEMONICS = {
  "p":"px",
  "e":"em",
  "r":"rem",
  "i":"in",
  "c":"cm",
  "m":"mm",
  "x":"ex",
}

#}}}
#{{{ Globals

def error_handler( msg ):
  pass
log_err = error_handler


class a_preprocess_error( Exception ):
  def __init__( me, errorcode ):
    me.errorcode = errorcode

APpDIR = path.dirname( path.realpath(__file__) )

def replace_list( string, thelist ):
  newstring = ""
  lastend = 0
  for start, end, replacement in thelist:
    newstring += string[lastend:start] + replacement
    lastend = end
  newstring += string[lastend:]
  return newstring

def nested_regex( str, start, end ):
  """
  For a given "str" where "start" points to openchar like (,{, or whatever
  and "end" points after the first found ),},... find the last closing character
  in nested manner
  Return new "end" after last nested character or -1 if nesting not closed
  """
  #print "* %d %d %s" % (start,end, str)
  openchar = str[start]
  start = start+1 # compatibility with the end
  closechar = str[end-1]
  while True:
    inner = str.count( openchar, start, end)
    # if at least one openchar before previous closegchar
    if inner > 0:
      start = end
      # for every missing closechar
      for i in range(inner):
        end = str.find( closechar, end ) 
        if end == -1:
          break
        else:
          end +=1 # end has to be after the last
      if end == -1:
        break
    else:
      break # no more char to close
  return end




#}}}
#{{{ Class a_cut

NESTEdRE = re.compile( r"\*/" )
class a_cut( object ):
  """
  A cut string. For us this is CSS content where comments are cut out,
  but their positions and values are stored and can be recovered.
  Positions are shifting when content is changing, accordingly.
  """
  def __init__( me, str ):
    me.str = str # visible content
    me.oryg = str # oryginal content
    me.cutregister = [] # register with cut comments and positions

  def __str__( me ):
    return me.str

  def set_str( me, str ):
    me.str = str

  # it has to preserve cut register
  def append( me, str ):
    me.str += str

  def register_append( me, str ):
    (afterlastcut, _) =  me.last_cut_dinstances()
    me.cutregister.append( ( afterlastcut, str ) )


  def cut_and_save( me, indexes, a ):
    """ 
    cut data (like comments) and save them in the register for later recover
    """
    result = ""
    last = 0
    fromlastsaved = 0
    for start,end in indexes:
      result += me.str[ last : start ]
      tosave = me.str[ start: end ]
      # OK, removed. Now save in the register only if
      # 1. comments in the output are turned on
      # or
      # 3. comment doesn't contain exclamation under 3rd letter
      fromlastsaved += start-last
      if not a.no_comments or (  len(tosave)>2 and tosave[2] == "!"  ):
        # extract cpp comments
        if tosave[:2] == "//":
          tosave = "/*" + tosave[2:] + "*/"
        # re-nest nested comments
        tosave = NESTEdRE.sub( "*-/", tosave[:-2] ) + tosave[-2:]
        #
        me.cutregister.append( ( fromlastsaved, tosave ) )
        fromlastsaved = 0
      last = end
    result += me.str[ last : ]
    me.str = result

  def recover_from_save( me ):
    """
    recover data (like comments) from register
    """
    counter=0
    for pos,data in me.cutregister:
      counter += pos
      me.str = me.str[ : counter ] + data + me.str[ counter : ]
      counter += len(data)
    me.cutregister = []

  def last_cut_dinstances( me ):
    """ get ( characters after last cut, and last cut absolute position ) """
    # absolute register position, because register keeps only relative
    absolutregpos = 0
    for cut in me.cutregister:
      absolutregpos += cut[0]
    return ( len(me.str) - absolutregpos, absolutregpos )

    
  def replace_preserving( me, indexeswithdata, merge = False ):
    """
    For (start,end,stringorcut) in indexeswithdata:
      substitute start:end by stringorcut

    Update cut register for new positions !
    If merge == True, merge cutregisters from string_or_cut (has to be a cut)
    Delete comments between start:end.
    """
    if indexeswithdata:
      newstr = ""  # substituted string, concatenated by iteration
      laststridx = 0  # pos of last character in string
      newcutreg = []  # updated cut register, constructed by iteration
      lastregidx = 0  # pos of last visited record in register
      # absolute register position,
      # because register keeps only relative position from last record.
      absolutregpos = 0

      # following loop assumes indexeswithdata and cutregister are sorted!
      again = False  # flag for visiting register record more than once
      afterremovefix = 0  # when removing comments

      for start,end,stringorcut in indexeswithdata:
        # SUBSTITUTE
        newstr += me.str[ laststridx : start ] + str(stringorcut)
        laststridx = end # for next substitude iteration
        merged = False

        # starting from lastregidx up to place where "cut" is found
        # and break then!
        for cut in me.cutregister[lastregidx:]:
          if not again:
            absolutregpos += cut[0]

          if afterremovefix:
            cut = ( cut[0] + afterremovefix, cut[1] )
            afterremovefix = 0

          # Main condition to check if cut should be updated
          # it works because als cuts before are skipped in the
          # "else" statement below
          if absolutregpos > start:
            if absolutregpos < end:
              # delete this register (together with content)
              if again:
                try:
                  deleted = newcutreg.pop()
                except IndexError:
                  log_err("COD internal error which never should happened\n")
                  sys.exit(42)
                again = False
              else:
                deleted = cut
              # fix next register
              afterremovefix = deleted[0]
              lastregidx += 1  # skip this record next iteration
              continue  # it's not needed, but for visibility
            else:
              #how much substitute changed text
              delta = len(str(stringorcut)) - (end-start)
              if not again:
                # update register from oryginal
                newcutreg.append(  ( cut[0] + delta, cut[1] )  )
                again = True
              else:
                #update register alredy updated
                newcutreg[-1] = ( newcutreg[-1][0] + delta, newcutreg[-1][1] )
              if merge:
                ( merged, newcutreg ) = me.merge_cutregister_when_replace(
                  stringorcut,
                  newcutreg,
                  newstr)
              break
          else:
            if not again:
              # copy record without updating. not needed
              newcutreg.append( cut ) 
            lastregidx += 1 # skip this record next iteration
            again = False

        # do merging if not before other registters - appending
        if merge and not merged:
          ( merged, newcutreg ) = me.merge_cutregister_when_replace(
            stringorcut,
            newcutreg,
            newstr,
            tail = True) 

      # copy rest of the string
      newstr += me.str[ laststridx : ]
      # copy rest of register
      againfix = 1 if again else 0
      for i in range( lastregidx + againfix, len(me.cutregister) ):
        newcutreg.append( me.cutregister[i] )
      
      # save str and register
      # We need to do it at the end because all indexes are from oryginal string
      me.str = newstr
      me.cutregister = newcutreg

  def merge_cutregister_when_replace(
        me,
        stringorcut,
        newcutreg,
        newstr,
        tail = False 
    ):
    result = False
    if stringorcut != []:

      (mergefilling, mergeabsolute) = stringorcut.last_cut_dinstances()
      if tail:
        lastindex = None
      else:
        lastindex = -1

      a = 0
      for cut in newcutreg[:lastindex]:  # the last included cut is before -1
        a += cut[0]
      # len() - len() means previous text
      oldfilling = len(newstr) - len(str(stringorcut)) - a
      mergecut = stringorcut.cutregister

      if mergecut:
        mergecut[0] = ( mergecut[0][0] + oldfilling, mergecut[0][1] )
        if not tail:
          newcutreg = newcutreg[:-1] + mergecut + \
            [ ( newcutreg[-1][0] - oldfilling - mergeabsolute, newcutreg[-1][1] ) ]
        else:
          newcutreg += mergecut
      
      result = True
    return ( result, newcutreg )

#}}}
#{{{ Comments

COMMENTsRE = re.compile(r"""
                        \\"  |  # should it be before quotes ? probably
                        \\'  |
                        "    |
                        '    |
                        \n   |
                        //   |
                        /\*  |
                        \*/
                        """, re.X)

def rm_comments( cut, a ):
  nocomment = 0 # no inside comment
  c = 1 # c-like comments, but nested
  cpp = 2 # c++like comments
  doublequote = 3 # strings " \" "
  singlequote = 4 # strings ' \' '

  mode = nocomment
  clevel = 0  # nesting level of c-like comments
  matchesidx = []

  # in pure RE we cannot find nestesd structuries
  # so we are just finding all boundires and parse it here
  matches = COMMENTsRE.finditer( str(cut) )
  start = 0
  for i in matches:
    m = i.group()
    #**  PROCESS modes
    if mode == doublequote:
      if m == '"':
        mode = nocomment
    elif mode == singlequote:
      if m == "'":
        mode = nocomment
    elif mode == cpp:
      if m == "\n":
        matchesidx.append( ( start, i.end()-1 ) ) # -1 because without \n
        mode = nocomment
    elif mode == c:
      if m == "/*":
        clevel += 1
      elif m == "*/":
        clevel -= 1
      if clevel == 0:
        matchesidx.append( ( start, i.end() ) )
        mode = nocomment
    #**  INIT modes
    else:
      if m == '"':
        mode = doublequote
      elif m == "'":
        mode = singlequote
      elif m == "//":
        start = i.start()
        mode = cpp
      elif m == "/*":
        start = i.start()
        mode = c
        clevel += 1
    
  cut.cut_and_save( matchesidx, a )

#}}}
#{{{ Defines

# TODO str supp
DEFINEsBLOCkRE = re.compile( r"""
  @cod-defines?
  \s*
  ({
  .*?
  })
                            """, re.X|re.S|re.M ) 

DEFINeNAMeCHAR = r"[-\w]"
# TODO str supp
DEFINEsRE = re.compile( r"""
  (?P<name>%s+)   # some freedom in naming
  [ \t\r\f\v]*       # not \n! can be empty when no body
  (?P<body>.*?)      # can be empty
  $                  # end of line or text
                       """ % DEFINeNAMeCHAR, re.X|re.M ) 

class a_defines(object):
  def __init__( me ):
    # list of 
    #(name, body, pat_in, pat_out)
    # where pat_in is pattern maching name
    # to use inside @cod-define
    # pat_out - everywhere outside
    # This list is sorted with longer at the front
    # to avoid substring substitutions inside @cod-defines
    me.db = []
  def add_def( me, name, body ):
    # because of - in arythmeticts, this is not possible
    #pat1 = r"(?<!%s)" % DEFINeNAMeCHAR
    pat1 = r"\b"
    pat2 = re.escape( name ) 
    #pat3 = r"(?!%s)" % DEFINeNAMeCHAR
    pat3 = r"\b"
    pat4 = r"(?:\s*(\(.*?\)))?"  # optional parentheses

    patin = re.compile( pat2 + pat4 ) 
    patout = re.compile( pat1 + pat2 + pat3 + pat4, re.S ) 

    i = 0
    while i < len(me.db):
      if len(name) >= len(me.db[i][0]):
        break
      i += 1
    me.db.insert(i, (name, body, patin, patout))

  def get_all(me, inside):
    if inside:
      return [(x[2], x[1]) for x in me.db]
    else:
      return [(x[3], x[1]) for x in me.db]


def read_defines( cut ):
  defines = a_defines()
  cos = str(cut)
  blocks = DEFINEsBLOCkRE.finditer( cos )
  to_replace = []
  for b in blocks:
    nestedend = nested_regex( cos, b.start(1), b.end(1) )
    if nestedend == -1:
      continue
    definesblock = cos[ b.start(1)+1 : nestedend-1 ]

    to_replace.append( ( b.start(), nestedend, "" ) )

    definesmatch = DEFINEsRE.finditer( definesblock )
    for d in definesmatch:
      name = d.group("name")
      body = d.group("body")
      # self expand
      body = expand_defines( defines, body )
      #
      defines.add_def( name, body )
  cut.replace_preserving( to_replace )
  return defines

# TODO str supp
DEFINeARGUMENT = re.compile( r"_ARG(\d+)_" )


def expand_defines( defines, cutorstr ):
  inside = isinstance(cutorstr, str)

  for defpat, defbody in defines.get_all(inside):

    cos = str(cutorstr)
    defcandidate = re.finditer(defpat, cos)
    tocutit = []
    for d in defcandidate:
      newbody = defbody
      # find arguments
      arguments = []
      #TODO check if the previous end doesn't overlap current one
      # if arguments
      end = d.end()
      if d.group(1): 
        start = d.start(1)
        end = d.end(1)
        end = nested_regex( cos, start, end )
        if end == -1:
          continue

        argumentslist = cos[start+1:end-1].split(",")
        for a in argumentslist:
          arguments.append(a.strip())

      # apply arguments
      if arguments:
        highest = 0
        for arg in DEFINeARGUMENT.finditer( defbody ):
          no = int( arg.group(1) )
          if no > highest:
            highest = no
        #
        newbody = DEFINeARGUMENT.sub( lambda x: expand_argument(arguments, x, defbody), defbody)
        # append extra arguments at the end
        if highest < len(arguments):
          newbody += " " + " ".join( arguments[highest:] )

      # d.start() - begining of whole define
      tocutit.append((d.start(), end, newbody))

    if tocutit:
      if inside:
        cutorstr = replace_list(cutorstr, tocutit)
      else:
        cutorstr.replace_preserving(tocutit)

  return cutorstr
      
def expand_argument( arguments, matchobject, body ):
  no = int( matchobject.group(1) )
  try:
    return arguments[ no - 1]
  except IndexError:
    #log_err( "Missing argument for define: '%s'\n" % body ) 
    return ""

#}}}
#{{{ Medias

MEDIaBLOCkRE = re.compile( r"""
  @cod-medias?
  \s*
  {
  (.*?) # everything up to close
  }
                            """, re.X|re.S|re.M ) 

MEDIaNAMeCHAR = DEFINeNAMeCHAR
# TODO str supp
MEDIaRe = re.compile( r"""
  (?P<name>%s+)   # some freedom in naming
  [ \t\r\f\v]*       # not \n! can be empty when no body
  (?P<body>.*?)      # can be empty
  $                  # end of line or text
                       """ % MEDIaNAMeCHAR, re.X|re.M ) 

# TODO common base class for a_medias and a_defines
class a_media(object):
  def __init__( me ):
    # list of 
    # (name, body, @name)
    # where @name is word to find
    me.db = []
  def add_media( me, name, body ):
    me.db.append( (name, body, "@"+name) )

  def empty( me ):
    return len(me.db) == 0

  def find_index( me, atname ):
    index = 0
    for name,body,at in me.db:
      if atname == at:
        return index
      index += 1
    return None

  def get_breakpoints(me):
    return [(x[0], x[1]) for x in me.db]


def read_media(cut):
  media = a_media()
  blocks = MEDIaBLOCkRE.finditer( str(cut) )
  to_replace = []
  for b in blocks:
    mediasblock = b.group(1)
    to_replace.append( ( b.start(), b.end(), "" ) )

    mediamatch = MEDIaRe.finditer( mediasblock )
    for m in mediamatch:
      name = m.group("name")
      body = m.group("body")
      # self expand
      # Not for media # body = expand_defines( media, body )
      #
      media.add_media( name, body )
  cut.replace_preserving( to_replace )
  return media

def move_media( media, cut ):

  if not media.empty():

    rules = RULeRE.finditer( str(cut) )
    toreplace = []
    saved = [] # selected @media to place at the end of file
               # structure of tables and tuples 
               # cannot use OrderedDict because python2.6
    for n,b in media.get_breakpoints():
      saved.append( (n, b, []) )

    # faster would be just look for lines with @mediabreakpoints
    # but how to get selector then?
    for r in rules:
      
      selector = r.group(1)
      declarations = DECLARATIOnRE.finditer( str(cut), r.start(2), r.end(2) )
      for d in declarations:

        value = d.group("value")
        splitted = value.split()
        if len(splitted) > 0:
          idx = media.find_index( splitted[-1] )
          if idx is not None:
            decla = d.group().replace( splitted[-1], "" )  # remove @medianame
            for selectorsaved, declarationssaved in saved[idx][2]:
              if selectorsaved == selector:
                declarationssaved.append( decla )
                break
            else:
              saved[idx][2].append( ( selector, [ decla ] ) )
            toreplace.append( ( d.start(), 
                                d.end(), 
                                "" ) )
    cut.replace_preserving( toreplace )

    for medianame, mediabody, rules in saved:
      out = "@media %s {\n" % mediabody
      for selector, declarations in rules:
        out += "%s {\n" % selector
        for decla in declarations:
          out += "%s" % decla
        out += "}\n"
      out += "}\n"
      cut.register_append("/**  Breakpoint: %s  **/\n" % medianame)
      cut.append( out )

#}}}
#{{{ Arithmetics

# string support
ARITHMETIcRE = re.compile( r"""
    \s          # has to be sourrounded by white characters
    (           # main body - no white spaces
    (?:
    [()\-+*/.]| # possible operators
    \d+px?|     # digit with unit
    \d+%|       # ...
    \d+em?|
    \d+r(?:em)?|
    \d+in?|
    \d+cm?|
    \d+mm?|
    \d+e?x|
    \d+s|
    \d+pt|
    \d+pc|
    \d+         # has to be at the end - no unit
    )+
    )
    (?=\s)   
                       """,  re.X | re.S ) 
ARITHMETIcUNITsRE = re.compile( r"""
    px?|
    %|
    em?|
    r(?:em)?|
    in?|
    cm?|
    mm?|
    e?x|
    s|
    pt|
    pc
                       """,  re.X ) 
ARITHMETIcAtLEAStTWoRE = re.compile( r"""
    [\-+*/][\d(]
                       """,  re.X ) 

def reduce_arithmetic( cut ):
  tochange = []
  arith = ARITHMETIcRE.finditer( str(cut) )
  for a in arith:
    astr = a.group(1)
    if not ARITHMETIcAtLEAStTWoRE.search( astr ):
      continue # at least one operator and digit to be arithmetic expression
    ( expr, unit ) = get_arithmetic_units( astr )
    try:
      result = eval(expr, {})
    except SyntaxError:
      continue
    if "." not in expr:
      result = math.trunc( result )

    resultstr = str(result)
    if unit:
      resultstr += unit
    tochange.append( ( a.start(1), 
                       a.end(1), 
                       resultstr ) )
  cut.replace_preserving( tochange )
    
    
def get_arithmetic_units( a ):
  """naive assumption that units will be the same"""
  """ returns first found unit """
  # TODO unit recalc
  unit = None
  all = ARITHMETIcUNITsRE.finditer( a )
  for u in all:
    if unit is None:
      unit = u.group()
    else:
      if unit != u.group():
        log_err( "Wrong unit in the expression: '%s'\n" % a )
        pass 
  # remove units
  a = ARITHMETIcUNITsRE.sub( "", a )
  return (a, unit)

#}}}
#{{{ RGBA

# TODO str supp
# but maybe really not needed
RGBaRE = re.compile( r"""
    \W          # cannot be \b because of \#
    (           #
    \#          # don't forget to escape it
    [\dabcdefABCDEF]{8,8} # 8 positions
    )
    \b
                       """,  re.X | re.S)


def expand_rgba(cut):
  tochange = []
  rgba = RGBaRE.finditer( str(cut) )
  for c in rgba:
    color = c.group(1)
    colorstr = convert_rgba_hex_to_str( color )
    tochange.append( ( c.start(1), 
                       c.end(1), 
                       colorstr ) )
  cut.replace_preserving( tochange )

def convert_rgba_hex_to_str( color ):
  intvals = []
  pos = 1
  for x in range(4):
    hexstr = color[pos:pos+2]
    intvals.append(  int( hexstr, 16 )  ) 
    pos += 2
  intvals[3] = round( float(intvals[3])/255, 3 )
  # after round %g will remove trailing zeros
  return "rgba(%d,%d,%d,%.3g)" % tuple(intvals)
    
#}}}
#{{{ Apply Mnemonics

STRINgSUBRE = r"""
  (?P<string>
    "(?:[^"\\]+|\\.)*"
  | '(?:[^'\\]+|\\.)*'
  )
"""

RULeRE = re.compile(r"""
\s*([^;{}]+)\s*  # selector
{
  (  # main body
    (?:
      %s | # whole string or
      [^{] # any character outside whole string
           # exclude { in case of @media and @font
    )*?
  )
}
""" % STRINgSUBRE, re.S | re.X ) 

DECLARATIOnRE = re.compile( r"""
\s*   # consume all white space (only for @cod-media?)
(?P<param>[\w\-]+) # parameter
(?P<sep>[\s:]+) # optional separator
(?P<value>
  (?:
    %s | # whole string or 
    [^;\n] # any character outside whole string
  )+
) # value
(?P<delim>[;\n]?) # delimeter
""" % STRINgSUBRE, re.S | re.X ) 

# TODO str supp
VALUeRE = re.compile( r"([\w!%-]+)(\s*\(.*?\))?"  )
#VALUeRE = re.compile( r"([\w!%-]+)"  )
UNItRE = re.compile( r"\b\d+([a-z])\b" )
  
def apply_mnemonics( cut ):
  rules = RULeRE.finditer( str(cut) )
  toreplace = [] # has to be ordered
  for r in rules:

    declarations = DECLARATIOnRE.finditer( str(cut), r.start(2), r.end(2) )
    for d in declarations:

      if d.group("param") in PROPERTyMNEMONICS:
        toreplace.append( ( d.start("param"), 
                             d.end("param"), 
                             PROPERTyMNEMONICS[ d.group("param") ] ) )

      if not ":" in d.group("sep"):
        toreplace.append( ( d.start("sep"), 
                           d.start("sep"), # insert at the begining
                           ":" ) )


      values = VALUeRE.finditer( str(cut), d.start("value"), d.end("value") )
      for v in values:
        if v.group(1) in VALUeMNEMONICS:
          toreplace.append( ( v.start(1), 
                              v.end(1), 
                              VALUeMNEMONICS[ v.group(1) ] ) )
        else:
          units = UNItRE.finditer( str(cut), v.start(1), v.end(1) )
          for u in units:
            if u.group(1) in UNItMNEMONICS:
              toreplace.append( ( u.start(1), 
                                  u.end(1), 
                                  UNItMNEMONICS[ u.group(1) ] ) )



      if d.group("delim") == "\n":
        toreplace.append( ( d.start("delim"), 
                           d.start("delim"), # insert at the begining
                           ";" ) )

  cut.replace_preserving( toreplace )

#}}}
#{{{ Apply Prefixes

def apply_prefixes( cut ):
  cos = str(cut)
  toreplace = [] # has to be ordered

  rules = RULeRE.finditer( cos )
  for r in rules:

    declarations = DECLARATIOnRE.finditer( cos, r.start(2), r.end(2) )
    for d in declarations:

      toprefix = []

      if d.group("param") in PREFIXES:
        toprefix.append( d.group("param") )

      values = VALUeRE.finditer( cos, d.start("value"), d.end("value") )
      for v in values:
        if v.group(1) in PREFIXES:
          toprefix.append( v.group(1) )

      if toprefix:
        p = prefix_it( toprefix, PREFIXES, d.group() )
        toreplace.append( ( d.start(), d.start(), p ) )

  cut.replace_preserving( toreplace )

def apply_atrules_prefixes( cut ):
  cos = str(cut)
  toreplace = [] 

  for at in ATRULESPREFIXES: # "keyframes"
    atre = re.compile( r"@%s[^{}]*({.*?})" % at, re.S )
    atrules = atre.finditer( cos )
    for r in atrules:
      nestedend = nested_regex( cos, r.start(1), r.end(1) )
      if nestedend == -1:
        continue
      fullrule = cos[ r.start() : nestedend ]

      p = prefix_it( [at], ATRULESPREFIXES, fullrule )
      toreplace.append( ( r.start(), r.start(), p ) )

  cut.replace_preserving( toreplace )

def prefix_it( toprefix, table, text ):
  byprefix = {}
  order = [] # because no OrderedDict for 2.6
  for tp in toprefix:
    for p in table[ tp ]:
      if p in byprefix:
        byprefix[ p ] = byprefix[p].replace( tp, p+tp, 1 )
      else:
        byprefix[ p ] = text.replace( tp, p+tp, 1 )
        order.append( p )
  result = ""
  for p in order:
    result += byprefix[ p ]
  return result

#}}}
#{{{ Header

HEADErRE = re.compile( r"^//!(.*?)\n", re.S )
def extract_header( cut ):
  vendor=None
  m = HEADErRE.search( str(cut) )
  if m:
    vendor = m.group(1)
    cut.set_str(  HEADErRE.sub("", str(cut) )  )
  return vendor

def add_header( cut ):
  header = "/* Generated by oryginal css-on-diet v%s */\n"  % VERSION
  cut.set_str( header + str(cut) )

#}}} 
#{{{ Minify

MINIFySPACEsRE = re.compile( r"""
  %s           # whole string 
|
  # ; before } (and the spaces after it while we're here)
  \s* ; \s* ( } ) \s*
|
  # all spaces around meta chars/operators
  \s* ( [*$~^|]?= | [{};,>~+-] | !important\b ) \s*
|
  # spaces right of ( [ :
  ( [[(:] ) \s+
|
  # spaces left of ) ]
  \s+ ( [\])] )
|
  # spaces left (and right) of :
  \s+ ( : ) \s*
#  # but not in selectors: not followed by a {
#  (?!
#    (?:
#      [^{}"']+
#    | "(?:[^"\\]+|\\.)*"
#    | '(?:[^'\\]+|\\.)*'
#    )*
#    {
#  )
|
  # spaces at beginning/end of string
  ^ \s+ | \s+ \Z
|
  # double spaces to single
  (\s)\s+
""" % STRINgSUBRE, re.X|re.S|re.I)

def minify_spaces( css ):
  return MINIFySPACEsRE.sub( replace_spaces, css )

def replace_spaces( m ):
  """ this functions is workaround for python sre exception "unmatched groups"
  """
  out = ""
  for g in m.groups():
    if g:
      out += g
  return out

#}}}
#{{{ Includes

# TODO str supp
INCLUDEsBLOCkRE = re.compile( r"""
  @cod-includes?
  \s*
  {
  (.*?) # everything up to close
  }
""", re.X|re.S ) 
# TODO str supp
INCLUDEdFILeRE = re.compile( r"""
  \s*
  (["']?)
  (?P<file>.*?)
  \1
  \s*
  $
""", re.X|re.M ) 

def find_includes( cut ):
  result = []
  blocks = INCLUDEsBLOCkRE.finditer( str(cut) )
  to_replace = []
  delta = 0
  for b in blocks:
    includesblock = b.group(1)
    to_replace.append( ( b.start(), b.end(), "" ) )

    includedfiles = INCLUDEdFILeRE.finditer( includesblock )
    for i in includedfiles:
      filename = i.group("file") 
      if filename: # can be empty string because of surrounding spaces issue
        result.append( (filename, b.start() + delta ) )
    delta += b.start() - b.end()
  cut.replace_preserving( to_replace )
  return result

def get_nlcharacter( hdl ):
  nl = None
  if isinstance(hdl.newlines, str):
    nl = hdl.newlines
  elif isinstance(hdl.newlines, tuple):
    nl = choose_nlcharacter(hdl.newlines)
  return nl

def choose_nlcharacter( newlines ):
  if "\r\n" in newlines:
    nl = "\r\n" # priority for dos
  elif "\n" in newlines:
    nl = "\n" # than unix
  elif "\r" in newlines:
    nl = "\r" # than mac
  else: # None
    nl = "\n" # unix by default
  return nl


def include_files_recursiv( a, filename, included_sha1 ):
  if filename == "-":
    content = sys.stdin.read()
    directory = "" # current path
    nlcharacterlist = [ "\n" ]
  else:
    if not path.exists( filename ):
      log_err( "File \"%s\" can't be preprocess because it doesn't exist\n"
          % ( str(filename) ) ) 
      raise a_preprocess_error( 63 )
    try:
        with open(filename, "U") as fh:
          directory = path.dirname( path.realpath( filename ) )
          content = fh.read()
          nlcharacterlist = [ get_nlcharacter( fh ) ]
    except IOError as e:
      log_err( "I have problem reading '%s' file. Exception '%s'.\n" \
          % ( str(filename), str(e.strerror) ) )
      raise a_preprocess_error( 111 )
    except Exception as e:
      log_err( "I have weird problem probably with '%s' file. Exception '%s'.\n" \
          % ( str(filename), str(e) ) )
      raise a_preprocess_error( 32 )

  #
  sha1 = hashlib.sha1()
  sha1.update( content.encode('utf-8') )
  sha1 = sha1.digest()
  if sha1 in included_sha1:
    log_err( "File %s won't be included second time\n" % filename )
    return ( None, None )
  else:
    included_sha1.append( sha1 )
  contentcut= a_cut( content )
  flat_newlines( contentcut )
  extract_header( contentcut )
  rm_comments( contentcut, a )
  tomerge = []
  for infile, position in find_includes( contentcut ):
    alldirs = [directory] + a.include_dirs
    for dir in alldirs:
      inabsfile = path.join( dir, infile )
      if path.exists( inabsfile ):
        break
    else:
      # this is only for included files, so it is not at the top of this function
      log_err( "File \"%s\" can't be included because it doesn't exist" \
      " in any of these directories: %s\n" \
          % ( str(infile), str(alldirs) ) )
      raise a_preprocess_error( 67 )

    (incontentcut, innlcharacter) = include_files_recursiv ( a, inabsfile, included_sha1 )
    if incontentcut == None:
      continue
    nlcharacterlist.append( innlcharacter )
    tomerge.append( (position,position,incontentcut) )
  contentcut.replace_preserving( tomerge, merge=True )
  nlcharacter = choose_nlcharacter( nlcharacterlist )
  return (contentcut, nlcharacter)

def flat_newlines( cut ):
  cut.set_str( str(cut).replace("\\\n","") )

#}}}
#{{{ put_css_on_diet 

def put_css_on_diet( a, error_handler ):
  global log_err
  log_err = error_handler

  _profiler_start( a )
  contentcut = a_cut( "" ) # empty because it is meta cod file for cmd line args
  tomerge = []
  included_sha1 = []
  nlcharacterlist = [ ]
  for filename in a.cod_files:
    incontentcut, innlcharacter = include_files_recursiv ( a, filename, included_sha1 )
    if incontentcut == None:
      continue
    nlcharacterlist.append( innlcharacter )
    tomerge.append( ( 0, 0, incontentcut ) ) # 0 means at the end because contentcut is empty
  contentcut.replace_preserving( tomerge, merge = True )
  nlcharacter = choose_nlcharacter( nlcharacterlist )
  _profiler_point(a, "Includes")

  definesdict = read_defines( contentcut )
  expand_defines( definesdict, contentcut )
  _profiler_point(a, "Defines")
  reduce_arithmetic( contentcut )
  _profiler_point(a, "Arithmetics")
  expand_rgba( contentcut )
  _profiler_point(a, "RGBA")
  medias = read_media( contentcut )
  move_media( medias, contentcut )
  _profiler_point(a, "Medias")
  apply_mnemonics( contentcut )
  _profiler_point(a, "Mnemonics")
  if not a.no_prefix:
    apply_prefixes( contentcut )
    apply_atrules_prefixes( contentcut )
    _profiler_point(a, "Prefixer")

  contentcut.recover_from_save() 
  if not a.no_header:
    add_header( contentcut )
  _profiler_point(a, "Comments recover")

  content = str(contentcut)

  if a.minify_css:
    content = minify_spaces( content )
    _profiler_point(a, "Minifier")

  if nlcharacter is not None:
    content = content.replace("\n", nlcharacter)

  handleout = open(a.output, 'w') if a.output != "-" else sys.stdout

  handleout.write( content )
  if handleout is not sys.stdout:
    handleout.close()
  _profiler_point(a, "Writer")
  _profiler_end(a)

def _profiler_start( a ):
  if a.profile:
    _profiler_start.time = time.time()
    _profiler_start.initialtime = _profiler_start.time
    _profiler_start.file = open( a.profile, "w" )

def _profiler_point( a, label ):
  if a.profile:
    now = time.time()
    delta = now - _profiler_start.time
    _profiler_start.file.write("%20s %f\n" % (label, delta) )
    _profiler_start.time = now

def _profiler_end( a ):
  if a.profile:
    delta = time.time() - _profiler_start.initialtime
    _profiler_start.file.write("%s\n%20s %f\n" % 
       ("="*20 + "|" + "="*8, "Execution time", delta) )
    _profiler_start.file.close()

#}}}
#{{{ __main__

if __name__ == "__main__":

  try:
    import argparse
    optmode = False
  except:
    # python2.6 dependency
    import optparse as argparse
    optmode = True
    argparse.ArgumentParser = argparse.OptionParser
    argparse.ArgumentParser.add_argument = argparse.ArgumentParser.add_option

  parser = argparse.ArgumentParser(
    description= "CSS-On-Diet - preprocessor for CSS files - ver. %s" % VERSION,
    epilog="http://cssondiet.com"
  )

  parser.add_argument(
    '-o', '--output', metavar="output.css",
    default="-",
    help='output file to save CSS. If not given or "-" string, print to STDOUT'
  )
  parser.add_argument(
    '-c', '--no-comments', action="store_true",
    help='cut out all comments'
  )
  parser.add_argument(
    '-d', '--no-header', action="store_true",
    help="don't add header line"
  )
  parser.add_argument(
    '-p', '--no-prefix', action="store_true",
    help="don't add prefixes"
  )
  parser.add_argument(
    '-m', '--minify-css', action="store_true",
    help="Minify CSS result code. Implies --no-comments and --no-header"
  )
  parser.add_argument(
    '-I', '--include-dirs', metavar='dir[,dir...]',
    action='append', # repeating arguments
    help="List of additional directories to look for included files. " +\
         "Multiple dirs can be separated by commas or by multiple " +\
         "-I(--include-dirs) arguments."
  )
  parser.add_argument(
    '--profile',  metavar='file',
    help="Profile the preprocessing execution and save it to file"
  )
  parser.add_argument(
    '-v', '--version',  action="store_true",
    help="Print software and specification versions"
  )
  # FINISH
  if not optmode:
    parser.add_argument('cod_files', metavar='file.cod', nargs="*",
                        help='CSS-On-Diet file to preprocess.' +
                        ' Multiple files are joined.' +
                        ' If "-" given read from STDIN instead of file.')
    args = parser.parse_args()
  else:
    (args, leftargs) = parser.parse_args()
    args.cod_files = leftargs

  if args.version:
    print("Version %s (for specification %s)" % (VERSION, PROToVERSION))
    sys.exit(0)

  # has to be after args.version
  if len( args.cod_files ) < 1:
    sys.stderr.write("Error: Give at least one file to preprocess\n")
    sys.exit(1)

  stdinasfile = 0
  for f in args.cod_files:
    if f == "-":
      stdinasfile += 1

  if stdinasfile > 1:
    sys.stderr.write("Only one file can be STDIN (don't use hyphen twice)\n")
    sys.exit(175)

  if args.minify_css:
    args.no_comments = True
    args.no_header = True

  if args.include_dirs:
    result = []
    for i in args.include_dirs:
      result += i.split(",")
    args.include_dirs = result
  else:
    args.include_dirs = [] # more useful than None

  args.include_dirs = list( map( path.abspath, args.include_dirs ) )


  try:
    put_css_on_diet( args, sys.stderr.write )
  except a_preprocess_error as e:
    sys.exit( e.errorcode )
#}}}

# vim: set foldmethod=marker:
