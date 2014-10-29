CSS-On-Diet
===========

CSS-On-Diet is a preprocessor for CSS files. The key feature is mnemonics for frequently used properties, which are similar to Emmet abbreviations. Other goodies include intuitive media breakpoints, nested and single line comments, variables and mixins, a calculator, hexadecimal RGBA, minifier, ...

Much more information on [cssondiet.com](http://cssondiet.com)

Features
========

Use old CSS
-----------

    .element {
      letter-spacing: 2px;
      background-color: #1C6BA0;
    }

If all your CSS declarations are on separate lines you don't have to change anything

Remove colons
-------------

    .element {
      letter-spacing 2px
      background-color #1C6BA0
    }

In CSS-On-Diet colons and semicolons are optional

Use mnemonics
-------------

    .element {
      les 2p
      bac #1C6BA0
    }

Common CSS keywords have mnemonics. Parameters are 3 letters long, values 2, and units just 1 letter ([The list](http://cssondiet.com))

Medias Breakpoints
------------------

    @cod-media {
      tablet (min-width: 768px)
    }
    .element {
      les 2p
      les 3p @tablet
    }

Responsive Web Design was never so easy and intuitive

One line comments
-----------------

    .element {
      les 2p // why not 3?
      bac #1C6BA0 // deep ocean
    }

No need to remember to close those comments

Nested comments
---------------

    .element {
      /*
      les /*3p*/ 2p
      */
      bac #1C6BA0
    }

Now you can comment out code with other comment inside. Finally...
 
Arithmetics
-----------

    .element {
      les 3p-1
      bac #1C6BA0
    }

CSS needs calculations. That's more than sure.

Short RGBA
----------

    .element {
      les 3p-1
      bac #1C6BA0F1
    }

Just two more digits and you have transparency with your color

Variables
---------

    @cod-defines {
      sp2014 3p-1
      ocean #1C6BA0F1
    }
    .element {
      les sp2014
      bac ocean
    }

Defines are like variables. Write it once and use it anywhere. Stay DRY!

Mixins
------

    @cod-defines {
      sp2014 3p-1
      ocean bac #1C6BA0_ARG1_ ;\
            bai url("fish.png")
    }
    .element {
      les sp2014
      ocean(F1)
    }

Mixins can be anything placed anywhere. Arguments give them programming power.


Installation
============

Actually, in the current version *cod.py* is the only file you need it. 
Of course you need [Python](http://www.python.org) to launch it. 
Note that in the proper installation *cod* script is a copy of *cod.py*.

To perform proper installation you have following choices:

1. Use/install [pip](https://pip.pypa.io/en/latest/installing.html) 
and type `pip install CSSOnDiet` (that will download and install CSSOnDiet 
from [pypi](https://pypi.python.org/pypi))
2. Download archive from [CSS-On-Diet website](http://cssondiet.com/installation), 
unpack it and run `python setup.py install`
3. Or clone [this](http://github.com/wyderkat/css-on-diet) github repo 
and run also `python setup.py install` from it.


