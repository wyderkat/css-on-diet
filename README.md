CSS-On-Diet
===========

CSS-On-Diet is a preprocessor for CSS files. The key feature are mnemonics for frequently used properties and value names, which are similar to Emmet abbreviations. Other goodies include optional colons and semicolons, nested and one line comments, variables and mixins, calculator, hexadecimal RGBA.

Much more information on [www.cofoh.com/css-on-diet](http://www.cofoh.com/css-on-diet)

Features
========

Use old CSS
-----------

    .element {
      letter-spacing: 2px;
      background-color: #1C6BA0;
    }

If all your CSS declarations are in separate lines you don't have to change anything. Normal CSS can be mixed with CSS-On-Diet.

Remove colons
-------------

    .element {
      letter-spacing 2px
      background-color #1C6BA0
    }

In CSS-On-Diet colons and semicolons are optional.

Use mnemonics
-------------

    .element {
      les 2p
      bac #1C6BA0
    }

Common CSS keywords have mnemonics. Parameters are 3 letters long, values 2, and units just 1 letter ([The list](http://www.cofoh.com/css-on-diet-LATEST))

One line comments
-----------------

    .element {
      les 2p // why not 3?
      bac #1C6BA0 // deep ocean
    }

One line comments finish at the end of the line. No need to close it anymore.

Nested comments
---------------

    .element {
      /*
      les /*3p*/ 2p
      */
      bac #1C6BA0
    }

Now you can comment out code with other comment. Finally...

Arithmetics
-----------

    .element {
      les 3p-1
      bac #1C6BA0
    }

CSS doesn't need complicated calculations. But it needs some basic operations.

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
      ocean #1C6BA0_ARG1_
    }
    .element {
      les sp2014
      bac ocean(F1)
    }

Mixins are defines with arguments. Easy to use but powerful syntax.


Installation from TGZ file
==========================

Unpack TGZ file and *cod* Python script is all you need. 

Install Python (ver 2.7.x preferable) if you don't have it.

