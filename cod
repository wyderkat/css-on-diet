#!/usr/bin/env python
###
# Copyright 2014 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##
VERSION = "1.2"
PROToVERSION = "1.2"

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
  "da":"dashed",
  "db":"double",
  "de":"default",
  "do":"dotted",
  "ea":"ease",
  "ei":"ease-in",
  "eo":"ease-out",
  "fi":"fixed",
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
  "ri":"right",
  "rx":"repeat-x",
  "ry":"repeat-y",
  "so":"solid",
  "st":"static",
  "ta":"table",
  "to":"top",
  "tr":"transparent",
  "un":"underline",
  "up":"uppercase",
  "vi":"visible",
  "wh":"white",
}

UNItMNEMONICS = {
  "p":"px",
  "e":"em",
  "i":"in",
  "c":"cm",
  "m":"mm",
  "x":"ex",
}

import re
import sys
from os import path
import hashlib

def error_handler( msg ):
  pass
log_err = error_handler

class a_preprocess_error( Exception ):
  def __init__(me, errorcode):
    me.errorcode = errorcode



APpDIR = path.dirname( path.realpath(__file__) )

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

  def cut_and_save( me, indexes ):
    """ 
    cut data (like comments) and save them in register for later recover
    """
    result = ""
    last = 0
    for start,end in indexes:
      result += me.str[ last : start ]
      tosave = me.str[ start: end ]
      tail = -2 # not to re-nest
      # extract cpp comments
      if tosave[:2] == "//":
        tosave = "/*" + tosave[2:] + "*/"
        tail = -2
      # re-nest nested comments
      tosave = NESTEdRE.sub( "*-/", tosave[:tail] ) + tosave[tail:]
      #
      me.cutregister.append( ( start-last, tosave ) )
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
    absolutregpos = 0 # absolute register position, because register keeps only relative 
    for cut in me.cutregister:
      absolutregpos += cut[0]
    return ( len(me.str) - absolutregpos, absolutregpos )

    
  def replace_preserving( me, indexeswithdata, merge = False ):
    """
    For start,end,stringorcut in indexeswithdata:
      substitute start:end by stringorcut
    Update cut register for new positions !
    If merge == True, merge cutregisters from string_or_cut (has to be cut)
    """
    if indexeswithdata:
      newstr = "" # substituted string, concatenated by iteration
      laststridx = 0 # pos of last character in string
      newcutreg = [] # updated cut register, constructed by iteration
      lastregidx = 0 # pos of last visited record in register
      absolutregpos = 0 # absolute register position, because register keeps only relative 
      # position from last record. 

      # following loop assumes indexeswithdata and cutregister are sorted!
      again = False # flag for visiting register record more than once 
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
          # condition to check if cut should be updated
          # it works because als cuts before are skipped in the 
          # "else" statement below
          if absolutregpos > start:
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
      #
      me.cutregister = []
      # TODO this should be changed to removing deleted comments. 
      fixnext = 0 # fix next pos which is relative to previous 
      for pos,data in newcutreg:
        pos += fixnext
        fixnext = 0
        if pos < 0: # negative registers
          # remove them
          pass
          # uncomment if we want to preserve negative comments
          #me.cutregister.append( (0, data) )
          fixnext = pos
        else:
          me.cutregister.append( (pos, data) )

  def merge_cutregister_when_replace(
        me,
        stringorcut,
        newcutreg,
        newstr,
        tail = False 
    ):
    result = False
    if stringorcut != []:

      (mergefilling, mergeabsolute) =  stringorcut.last_cut_dinstances()
      # TODO can be on fly
      if tail:
        lastindex = None
      else:
        lastindex = -1

      a = 0 
      for cut in newcutreg[:lastindex]: # the last included cut is before -1
        a += cut[0]
      oldfilling = len(newstr) - len(str(stringorcut)) - a # len() - len() means previous text
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



COMMENTsRE = re.compile( r"""
                        \\"  |  # should it be before quotes ? probably
                        \\'  |
                        "    |
                        '    |
                        \n   |
                        //   |
                        /\*  |
                        \*/  
                        """, re.X ) 

def rm_comments( cut ):
  nocomment = 0 # no inside comment
  c = 1 # c-like comments, but nested
  cpp = 2 # c++like comments
  doublequote = 3 # strings " \" "
  singlequote = 4 # strings ' \' '

  mode = nocomment
  clevel = 0 # nesting level of c-like comments
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
    
  cut.cut_and_save( matchesidx )

# TODO string support
DEFINEsBLOCkRE = re.compile( r"""
  @cod-defines?
  \s*
  {
  (.*?) # everything up to close
  }
                            """, re.X|re.S ) 

DEFINeNAMeCHAR = r"[-\w]"
# TODO string support
DEFINEsRE = re.compile( r"""
  (?P<name>%s+)   # some freedom in naming
  [ \t\r\f\v]*       # not \n! can be empty when no body
  (?P<body>.*?)      # can be empty
  $                  # end of line or text
                       """ % DEFINeNAMeCHAR, re.X|re.M ) 

class a_defines(object):
  def __init__( me ):
    me.dictin = {}
    me.dictout = {}
  def add_def( me, name, body ):
    pat1 = r"(?<!%s)" % DEFINeNAMeCHAR
    pat2 = re.escape( name ) 
    pat3 = r"(?!%s)" % DEFINeNAMeCHAR
    pat4 = r"(?:\s*\((.*?)\))?" # optional parentheses

    patin = re.compile( pat2 + pat4 ) 
    patout = re.compile( pat1 + pat2 + pat3 + pat4 ) 

    me.dictin[name] = (body, patin)
    me.dictout[name] = (body, patout)
  def get_all(me, out):
    if out:
      return me.dictout.values()
    else:
      return me.dictin.values()

def read_defines( cut ):
  defines = a_defines()
  blocks = DEFINEsBLOCkRE.finditer( str(cut) )
  to_replace = []
  for b in blocks:
    definesblock = b.group(1)
    to_replace.append( ( b.start(), b.end(), "" ) )

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

# TODO strings support
DEFINeARGUMENT = re.compile( r"_ARG(\d+)_" )

def expand_defines( defines, cutorstr ):
  if type( cutorstr ) == type( "" ):
    cut = False
  else:
    cut = True
  
  for defbody,defpat in defines.get_all( cut ):

    defcandidate = re.finditer( defpat, str(cutorstr) )
    tocutit = []
    for d in defcandidate:
      # find arguments 
      argumentsstring = d.group(1)
      arguments = []
      if argumentsstring:
        argumentslist = argumentsstring.split(",")
        for a in argumentslist:
          arguments.append( a.strip() )
      # apply arguments
      if arguments:
        defbody = DEFINeARGUMENT.sub( 
          lambda x: expand_argument(arguments,x), defbody )

      if cut:
        tocutit.append( ( d.start(), 
                          d.end(), 
                          defbody ) )
      else: # cut object
        cutorstr = cutorstr[:d.start()] + defbody + cutorstr[d.end():]

    if tocutit:
      cutorstr.replace_preserving( tocutit )

  return cutorstr
      
def expand_argument( arguments, matchobject ):
  no = int( matchobject.group(1) )
  try:
    return arguments[ no - 1]
  except IndexError:
    # TODO log
    return ""

# string support
ARITHMETIcRE = re.compile( r"""
    \s          # has to be sourrounded by white characters
    (           # main body - no white spaces
    (?:
    [()\-+*/.]| # possible operators
    \d+px?|     # digit with unit
    \d+%|       # ...
    \d+em?|
    \d+in?|
    \d+cm?|
    \d+mm?|
    \d+e?x|
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
    in?|
    cm?|
    mm?|
    e?x|
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
      continue # at least one operator and digit to be arythmetic expression
    ( expr, unit ) = get_arithmetic_units( astr )
    try:
      result = eval(expr, {})
    except SyntaxError:
      continue
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
  # TODO unit recalculations
  unit = None
  all = ARITHMETIcUNITsRE.finditer( a )
  for u in all:
    if unit==None:
      unit = u.group()
    else:
      if unit != u.group():
        pass # wrong unit - TODO 
  # remove units
  a = ARITHMETIcUNITsRE.sub( "", a )
  return (a, unit)

# TODO string support - but maybe really not needed
RGBaRE = re.compile( r"""
    \W          # cannot be \b because of \#
    (           # 
    \#          # don't forget to escape it
    [\dabcdefABCDEF]{8,8} # 8 positions
    )
    \b
                       """,  re.X | re.S ) 
def expand_rgba( cut ):
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

    

STRINgSUBRE = r"""
  (?P<string>
    "(?:[^"\\]+|\\.)*"
  | '(?:[^'\\]+|\\.)*'
  )
"""

SEtRE = re.compile( r"""
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

RULeRE = re.compile( r"""
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

# TODO string support, better parentheses
VALUeRE = re.compile( r"(\S+\s*\(.*?\)|\S+)"  )
UNItRE = re.compile( r"\b\d+([a-z])\b" )
  
def put_on_diet( cut ):
  sets = SEtRE.finditer( str(cut) )
  abbmatch = [] # has to be ordered
  for s in sets:

    rules = RULeRE.finditer( str(cut), s.start(1), s.end(1) )
    for rule in rules:

      if rule.group("param") in PROPERTyMNEMONICS:
        abbmatch.append( ( rule.start("param"), 
                             rule.end("param"), 
                             PROPERTyMNEMONICS[ rule.group("param") ] ) )

      if not ":" in rule.group("sep"):
        abbmatch.append( ( rule.start("sep"), 
                           rule.start("sep"), # insert at the begining
                           ":" ) )


      values = VALUeRE.finditer( str(cut), rule.start("value"), rule.end("value") )
      for val in values:
        if val.group(1) in VALUeMNEMONICS:
          abbmatch.append( ( val.start(1), 
                               val.end(1), 
                               VALUeMNEMONICS[ val.group(1) ] ) )
        else:
          units = UNItRE.finditer( str(cut), val.start(1), val.end(1) )
          for unit in units:
            if unit.group(1) in UNItMNEMONICS:
              abbmatch.append( ( unit.start(1), 
                                   unit.end(1), 
                                   UNItMNEMONICS[ unit.group(1) ] ) )



      if rule.group("delim") == "\n":
        abbmatch.append( ( rule.start("delim"), 
                           rule.start("delim"), # insert at the begining
                           ";" ) )

  cut.replace_preserving( abbmatch )


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
   # TODO this is CPU killer
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

# TODO string support
INCLUDEsBLOCkRE = re.compile( r"""
  @cod-includes?
  \s*
  {
  (.*?) # everything up to close
  }
""", re.X|re.S ) 
# TODO string support
INCLUDEdFILeRE = re.compile( r"""
  \s*
  (["']?)
  (?P<file>.+?)
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
      result.append( (filename, b.start() + delta ) )
    delta += b.start() - b.end()
  cut.replace_preserving( to_replace )
  return result

def get_nlcharacter( hdl ):
  nl = None
  if type(hdl.newlines) == type(""):
    nl = hdl.newlines
  elif type(hdl.newlines) == type(()):
    nl = choose_nlcharacter( hdl.newlines )
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


def put_css_on_diet( a, error_handler ):
  global log_err
  log_err = error_handler

  contentcut = a_cut( "" ) # empty because it is meta cod file for cmd line args
  tomerge = []
  included_sha1 = []
  nlcharacterlist = [ ]
  for filename in a.cod_files:
    incontentcut, innlcharacter = include_files_recursiv ( filename, included_sha1 )
    if incontentcut == None:
      continue
    nlcharacterlist.append( innlcharacter )
    tomerge.append( ( 0, 0, incontentcut ) ) # 0 means at the end because contentcut is empty
  contentcut.replace_preserving( tomerge, merge = True )
  nlcharacter = choose_nlcharacter( nlcharacterlist )

  definesdict = read_defines( contentcut )
  expand_defines( definesdict, contentcut )
  reduce_arithmetic( contentcut )
  put_on_diet( contentcut )
  #TODO where it should be
  expand_rgba( contentcut )

  if not a.no_comments:
    contentcut.recover_from_save() 
  if not a.no_header:
    add_header( contentcut )

  content = str(contentcut)

  if a.minify_css:
    content = minify_spaces( content )

  if nlcharacter != None:
    content = content.replace("\n", nlcharacter )

  handleout = open(a.output, 'w') if a.output!="-" else sys.stdout

  handleout.write( content )
  if handleout is not sys.stdout:
    handleout.close()

def include_files_recursiv( filename, included_sha1 ):
  try:
    with open(filename, "U") as fh:
      directory = path.dirname( path.realpath( filename ) )
      content = fh.read()
      nlcharacterlist = [ get_nlcharacter( fh ) ]
  except IOError as e:
    log_err( "I have problem including '%s' file. Exception '%s'.\n" \
        % ( str(filename), str(e.strerror) ) )
    raise a_preprocess_error( 11 )
  except Exception as e:
    log_err( "I have weird problem probably with '%s' file. Exception '%s'.\n" \
        % ( str(filename), str(e) ) )
    raise a_preprocess_error( 12 )

  #
  sha1 = hashlib.sha1()
  sha1.update( content.encode('utf-8') )
  sha1 = sha1.digest()
  if sha1 in included_sha1:
    # TODO log 
    return ( None, None )
  else:
    included_sha1.append( sha1 )
  contentcut= a_cut( content )
  extract_header( contentcut )
  rm_comments( contentcut )
  tomerge = []
  for infile, position in find_includes( contentcut ):
    #print ">>> infile=%s at position=%d in %s" % ( infile, position, filename )
    infile = path.join( directory, infile )
    (incontentcut, innlcharacter) = include_files_recursiv ( infile, included_sha1 )
    if incontentcut == None:
      continue
    nlcharacterlist.append( innlcharacter )
    tomerge.append( (position,position,incontentcut) )
  contentcut.replace_preserving( tomerge, merge=True )
  nlcharacter = choose_nlcharacter( nlcharacterlist )
  return (contentcut, nlcharacter)

if __name__ == "__main__":

  import argparse
  parser = argparse.ArgumentParser(
    description=
"""CSS On Diet
===========
Preprocessor for CSS files.
-------------------------
www.cofoh.com/css-on-diet""",
    formatter_class=argparse.RawDescriptionHelpFormatter,
  )

  parser.add_argument('cod_files', metavar='file.cod', nargs="+",
                      help='Css-on-diet file list to process')

  parser.add_argument(
    '-o', '--output', metavar="output.css",
    default="-",
    help='output file to save result css. If not given or "-" string, print to STDOUT'
  )
  parser.add_argument(
    '-c', '--no-comments',  action="store_true",
    help='cut out all comments'
  )
  parser.add_argument(
    '-d', '--no-header',  action="store_true",
    help="don't add header line"
  )
  parser.add_argument(
    '-m', '--minify-css',  action="store_true",
    help="Minify CSS result code. Implies --no-comments and --no-header"
  )
  # FINISH
  args = parser.parse_args()
  if args.minify_css:
    # because we don't operate on CUT object - TODO
    args.no_comments = True
    args.no_header = True

  try:
    put_css_on_diet( args, sys.stderr.write )
  except a_preprocess_error as e:
    sys.exit( e.errorcode )
