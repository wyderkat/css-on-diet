CSS-On-Diet Developer Guide
===========================

Introduction
============
*CSS-On-Diet* is a CSS Preprocessor with quite unique features. 
By intention it should be easy to use and fast to learn.
Other preprocessors seems to be focusing on adding new functions to *CSS* 
making the learning processes bit complicated and time consuming.
*CSS-On-Diet* focuses on writing *CSS* faster. 
Actually it not only makes writing, but also changing and reading it faster.

Lets use *COD* as a shortcut for *CSS-On-Diet* in following text. This document applies to 
[*COD Specification Version 1.5*](http://www.cofoh.com/css-on-diet-1.5), 
which is technical and detailed document. This Developer Guide is more human friendly version.

For more information check out 
[*COD Website*](http://www.cofoh.com/css-on-diet). 


Installation and usage
======================
As of current (1.5) version of 
[*COD Specification*](http://www.cofoh.com/css-on-diet-1.5), 
we deliver only command line tool.
It's written in Python, and called **cod**. 
We have plans for making windows application which will be easier to install.

Please note that COD files have *.cod* extension in their name and should be named like
that for editors support.

To check if **cod** is already installed try to check out version:

    cod -v


To install **cod** command line tool you have few choices. Lets start from most simple:

1. If you are using [Sublime Text Editor](http://www.sublimetext.com/), just type

        CSS-On-Diet

    in the Install Package box. The *COD* editor plugin includes **cod** command line tool,
    and it's connected to the editor's build system. So when you save file with *.cod* extensions,
    syntax will be highlighted and file will be compiled to *CSS* when build command is executed. 

    Note that Package Controller which provides Install Package box has to be installed separately
    from [here](https://sublime.wbond.net/installation).

2. If you have installed Python (default for Linux and MacOS), just use 
   [pip installator](https://pip.pypa.io/en/latest/installing.html). 

        pip install CSSOnDiet

   That's recommend and most flexible way.  On some systems *pip* command is not installed by
   default. You have to [install it](https://pip.pypa.io/en/latest/installing.html) first. 

3. You can also download latest *COD* package from [our website](http://www.cofoh.com/css-on-diet),
   unpack it like this (or other way you prefer):

        tar xfvz CSSOnDiet-1.5.tar.gz
   
   get inside unpacked directory and execute:
       
        python setup.py install

Note that only 1st choice doesn't require Python. Sublime Text Editor has embedded Python
runtime. But it doesn't give you access to **cod** script on system level, just from that editor.

Usage
-----

Command line tool **cod** preprocesses *COD* files:

    cod input.cod -o output.css

Add -m argument to minify your *CSS*:

    cod input.cod -o output.css -m

Check out more options from help message:
  
    cod -h


Formatting 
==========

In order to make *CSS* writing faster colons and semicolons in *COD* are not needed. It was always
annoying for me to put colon after every first word and semicolon at the end of the line.  Why to
use colons and semicolons if they are always at the same position?

    display: none;
    display none;
    display: none
    display none

In *COD* all 4 lines above have the same meaning. If you question that feature will lets write *CSS*
faster, I agree that's not big time saver. But wait for the next chapter, when you will learn more
about *COD* mnemonics. Just to have a quick look, compare this line:

    dis no

to this:

    dis: no;

That's 25% less characters. And not need to remember two more tokens is quite relief for my brain.

Optional semicolons put one restriction to our code: every *COD* declaration has to be on a separate
line. The newline character is replaced by semicolon in the final *CSS*. But there is a way to put
more declarations on a single line: just use semicolon in that case:

    display none; padding 0

For the price of extra semicolon (which is not extra in *CSS* anyway) we have two declaration on a
single line.

On the other hand, one line sometimes can be not enough for writing long declaration. You may want
to spread it across multiple lines to keep better visibility:

    background-image:
        linear-gradient(
          to right, 
          #fffdc2,
          #fffdc2 15%,
          #d7f0a2 15%,
          #d7f0a2 85%,
          #fffdc2 85%
        );

Unfortunately that code is not valid in *COD*. Every line is treated as a single declaration. In that
situation use escape character '\' just before new line to join lines before proper preprocessing
will take place:

    background-image: \
        linear-gradient( \
          to right, \
          #fffdc2, \
          #fffdc2 15%, \
          #d7f0a2 15%, \
          #d7f0a2 85%, \
          #fffdc2 85% \
        );

Just remember that '\' has to be exactly before a new line. Any spaces after will make it invalid.

Comments
--------

In *COD* we can use two types of comments. Standard *CSS* comments /\* \*/ and single line comments //.
The single line comment starts from the // sequence and finishes at the end of line. 
The standard *CSS* comments can be nested, unlike in pure *CSS*.

    /* comment /* inside another comment */ Still comment! */ 

That's very useful if you want to comment out code which already has comments in it.

    /*
    li {
      /* background: black; */
      background: white;
    }
    */



Mnemonics
=========
Mnemonics (abbreviations) are the sugar of *COD* preprocessor. The whole idea to create *COD* was
born when I was playing with [Emmet](http://emmet.io/). As you may know *CSS for Emmet* allows you
to type in your editor as few characters as possible to write *CSS* (Emmet is an editor plugin).
Because it's so useful for so many people why not use that all along *CSS* development? It's faster
to type in, faster to modify (very often change just one letter), and even faster to read it.

Mnemonics are available for 

1. properties names
2. declaration values
3. size units

Here are the lists of all mnemonics: [CSS-On-Diet
Mnemonics in the Specification](http://www.cofoh.com/css-on-diet-LATEST#Properties)

Every property mnemonic is 3 letters long. As you will start using them you will find few patterns
in their construction. Those patterns can faster your learning process significantly: 

- Most often mnemonic is equal to first 3 letters of a property name


        col = color
        wid = width


- If a property has more than one words in its name, first letters from every word are used

        lih = line-heigh
        les = letter-spacing
        pal = padding-left

- Shorthand properties (like background, font, padding, margin, etc.) have '-' hyphens in their names:

        pa- = padding
        ba- = background

- That hyphen character is changed to letter when we deal with not shorthand version

        par = padding-right
        bai = background-image

- 'border' has two hyphens because it is the most complicated property

        b-- = border
        bb- = border-bottom
        bbc = border-bottom-color
        bir = border-image-reapet

Mnemonics for values are just 2 letters long. Usually they are constructed from first two letters,
but not always.

    no = none
    rx = repeat-x
    bh = both
    db = double

Units mnemonics are only one letter and there is 6 of them. But even small change
(p = px, e = em) saves lot of typing when doing it over and over.

Here are the 3 lists of all mnemonics: [CSS-On-Diet
Mnemonics in the Specification](http://www.cofoh.com/css-on-diet-LATEST#Properties)


Medias
======

Media breakpoints is the feature which was added recently, but I'm quite proud of it.  It's the
biggest time saver in nowadays *CSS* development. Responsive Web Design is a must, no many will dare
to denied that. Copying your declarations together with selectors just to place it in the right
@media rule is a huge time waste.  And is so hard to keep eye on all versions of your declarations. 

Other preprocessors allows nesting media queries. That solves the readability problem. *COD* also
let us to write media specific declaration nested in ordinary rule.

    p {
      col #000000
      les 2p
      les 3p @Medium
      les 4p @Big
    }

But except that *COD* reduces required text to minimum, by extracting media breakpoints and using
just names for breakpoints.

    @cod-media {
      Medium  screen and (min-width : 480px)
      Big     screen and (min-width : 768px)
    }

Media breakpoint definition is written one per line in @cod-media rule.  First word a breakpoint
name, here Medium and Big. Rest of the line is a breakpoint definition which will be used in the
final @media rule.

Breakpoints usage doesn't need much explanation. Just put the breakpoint name at the end of the declaration and your are ready.
Above code produces following *CSS*:

    p {
      color: #000000;
      letter-spacing: 2px;
    }

    /**  Breakpoint: Medium  **/
    @media screen and (min-width : 480px) {
    p  {
      letter-spacing: 3px ;
    }
    }
    /**  Breakpoint: Big  **/
    @media screen and (min-width : 768px) {
    p  {
      letter-spacing: 4px ;
    }
    }

Breakpoints are expanded at the end of the file, in the order they were declared. The name of
the breakpoint can include letters, digits, underscore and hyphen and it's case sensitive.


Defines
=======

The most advanced (hope still easy to learn) feature are the defines. That what's behind variables,
mixins and macros/functions.

A define is a word which will be replaced by other word, multiple words, or any text at all.
Defines are declared in @cod-define rule, which is similar to already presented @cod-media. The rule
consist of declarations, one per line, where first word is a name and the rest of it is a define
body:

    @cod-define {
      BRAND-COLOR #431255
      boxspace 10p 20p
    }

Declared define can be used in any place of *COD* file (even before it's declaration):

    p {
      col BRAND-COLOR
      ma- boxspace
    }

Notice that you don't have to use '$' or any special character like in other preprocessors.
Although defines has to be surrounded by no words characters. A word in *COD*
consists of digits, letters, underscore and hyphen.

Defines can be use inside other defines

    @cod-define {
      A 10p
      B A+3p
    }

In that case only earlier declared defines are taken under consideration.  Unlike everywhere else,
inside @cod-defines they don't have to be whole words, but longer defines have precedence over
shorter

    @cod-define {
      BAC black
      BACGROUND red
      BRAND_BG BACGROUNDish
    }

In the above example BRAND\_BG will be expanded to "redish" color, not "blackGROUNDish".

Here is an example of a mixin:

    @cod-define {
      mixme mal 10p; pal 5p
    }

Because define body is always just one line long, semicolon is needed in our code. Although we can
use escaping character '\' before new line to join lines

    @cod-define {
      mixme mal 10p;\
            pal 5p
    }

That works, you can write one define on multiple lines, but semicolon is still needed.
'\' just joins lines, before real preprocessing. 

Because somebody may want to write mixin with curly braces in it (is it still called mixin??),
like this:

    @cod-define {
      mixme { mal 10p; pal 5p }
    }

The finale '}' in @cod-define has to be always on a separate line, to distinguish it with internal '}' characters.

Macros (functions) are defines with arguments:

    @cod-define {
      Ocean rgb(67,12,168,_ARG1_)
    }
    p {
      bac Ocean(0.50)
    }

Define name doesn't need any special signature to be a macro. 
Just in places where arguments will be expanded use *_ARG1_*, *_ARG2_*, *_ARG3_*, etc. That's all.

Includes
========
Including others files from *COD* file merges everything, resulting in a single *CSS* output. That
means a single HTTP request comparing to native @import rule. 

    @cod-include {
      file1.cod
      dir1/dir2/file2.css
    }

Every line represents a file path. Spaces at the beginning and ending are removed, but inside the line are preserved.

    @cod-include {
      directory/file with spaces.cod
    }

Eventually file path can be quoted.

    @cod-include {
      "dir/file.cod"
    }

Included files are put in @cod-include place in the final *CSS*. *COD* doesn't have problem when you
make an include loop. For example A includes B, B includes C and C includes A.  For every file *COD*
computes [a hash code](http://en.wikipedia.org/wiki/Hash_function) and only unique files are
included. So when you have two identical files but with different names, only first one will be
included. 

File paths are searched relative to parent file. That means relative to file which includes current
file.  If such file doesn't exist, include directories given for example as a command line -I
argument are checked.

    cod -I includedir,path/to/includes file1.cod

*COD* windows applications have easier ways to set up those paths.


Arithmetics & RGBA
==================
In the current version *COD* supports following operators: +, -, \*, /, (). To use them, whole
expression cannot contain spaces but has to be surrounded by spaces or new lines:

    word 10+2 20-3word

will be translated to

    word 12 20-3word

As you can see only the middle part is a correct expression.

If any of the operator arguments contains a dot in any number result will be real number. Otherwise it will be integer:

  21/5.0
  21/5

will produce:

  4.2
  4

If at least one of the arguments contains *COD* unit (px, p, em, e, ...) result will also have that unit

    20px+10 30+10%

gives:

    30px 40%

Unfortunately in the current version *COD* units cannot be converted from each other, so *COD* compiler will 
use first founded unit. So expression:

    2+3px+4in

give rather useless value of

    9px

Hexadecimal RGBA
----------------

One more handy feature. *COD* has fast way to write rgba() colors. Instead of normal 6 position color notation:

    #430CA8

add two more hex digits for alpha channel

    #430CA8CC

That gives us 8 bit resolution (256 possible alpha levels).
Generated *CSS* code will look like this:

    rgba(67,12,168,0.8)

The result alpha value is rounded to 3 digits after dot, so:

    #430CA8FD
    #430CA8FE
    #430CA8FF

will produce:

    rgba(67,12,168,0.992)
    rgba(67,12,168,0.996)
    rgba(67,12,168,1)

