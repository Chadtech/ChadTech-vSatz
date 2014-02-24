ChadTech

The following is a partially fictional conversation I had with a friend about ChadTech. I felt it served as a good introduction to what chadTech is.

Chad:

With my word processor, ChadTech, I have been successful at saving text in the image data. I feel this has been successful, and I am not even using the image file metadata. This makes me wonder, why arent all word processors using image files?

George:

Just because you can doesn't mean you should.

Chad:

But I totally should. Why shouldnt I?

Geroge:

If nothing else, size. One character of ascii is one byte. How much does it take ChadTech to store on character?

Chad:

One character in ChadTech is saved in doc[] as a number, up to four digits long.

George:

But you said it was an image file?

Chad:

Yeah, it produces an image. When you save your document it produces an image of your text, and in the margins beside text, the text data (doc[]) is stored in the pixel color values. When you open an image in ChadTech, it reads the text data from the pixels.

George:

Then why the image?

Chad:

Because I need letters to look at to read the document. The computer only needs data. Another cool thing about images, is you dont need ChadTech to read the documents ChadTech produces.

George:

PDFs are the same way. You still need an image viewer to read an image file.

Chad:

Well, alright. Thats true. Anyway, if I want to make a PDF, which is my current choice for making documents, I have to type some stuff up in word, or google docs, and many of the math and logic symbols I want to use are difficult to reach.

George:

Why not use Latex?

Chad:

Then I have to learn Latex. I just want to type stuff and have it appear in front of me in real time.

I could just keep using google docs, but making my own word processor also gives me the opportunity to make what I consider to be the ideal word processor, that being a black, screen shaped work area, with a raster terminal font. 

Also, do you mind if I abridge the hell out of this conversation and put it in the readme for ChadTech? I’ll make you say stuff like ‘Wow nice text editor Chad’.

George:

No I dont mind, and by the way, nice text editor Chad.

Chad:

Thanks George.

How to use ChadTech:

For the most part, and unless otherwise stated, if you press a key on your keyboard, the letter will show up in ChadTech, like any text editor. The features of ChadTech are controlled by hotkeys, which are listed below. All hotkeys should be pressed by holding down the first key, and then pressing the second, in that order and no other order.

ChadTech Commands:

  	CRTL then s                Save document

  	CTRL then o                Open document
  
  	CTRL then Backspace        Backspace 6 times

  	SHIFT then Backspace       Backspace exponetially

  	SHIFT then plus/equal key  Add superscript, or return to text if in subscript

  	SHIFT then minus key       Add subscript, or return to text if in superscript
  	
  	TAB then g                 Change from latin to greek letters

MATH SYMBOLS

  	Equals then period      Greater than or equal to

  	Equals then comma       Less than or equal to

  	Equals then d           Division sign (horizontal bar with a dot above and below)

  	Equals then a           Approximately equal to

  	Equals then p           Plus sign

  	Equals then m           Multiplication sign (dot)

  	Equals then q           QED (filled in square)

  	Equals then s           Square Root

  	Equals then l           'Plus or Minus'

  	Equals then f           Integral

  	Equals then n           Doesnt equal

  	Equals then g           Angle

  	Equals then t           A Triangle

  	Equals then r           Gradient

  	Equals then i           Infinity

  	Equals then c           Doesnt divide (as in 'divides' signs, not 'division' sign)

SET THEORY SYMBOLS

  	0 then e            'element of'

  	0 then d            'not element of'

  	0 then n            Null set

  	0 then u            Union

  	0 then i            Intersection

  	0 then s            'Sub set of'

  	0 then a            'Super set of'

  	0 then x            'not sub set of'

  	0 then z            'not super set of'

TURNSTILES

  	8 then s            Single Turnstile

  	8 then d            Double Turnstile

  	8 then x            Not single turnstile

  	8 then c            Not double turnstile

  	8 then l            Logical constant

FIRST ORDER AND PROPOSITIONAL LOGIC SYMBOLS

  	1 then e        Existential Quantifier

  	1 then a        'For all'

  	1 then i        Material Conditional, 'implies'

  	1 then f        If, and only if. Symbol also means 'equivalent' and 'congruent' in other context

  	1 then n        Negation

  	1 then x        Xor sign

  	1 then d        Nand sign

  	1 then period   And sign (not period)
  	
  	1 then b	Alternative negation sign (flat with lip, rather than wavy)

MODAL LOGIC SYMBOLS

  	2 then p          Possible

  	2 then n          Necessary
  
BRACKETS

  	c the  [        Left Chevron

  	c then ]        Right Chevron
  	
ALEXANDER HAMILTON

	4 then a		Second quadrant of Alexander Hamilton's portrait
	
	4 then l 		First quadrant of Alexander Hamilton's portrait
	
	4 then e 		Third quadrant of Alexander Hamilton's portrait
	
	4 then x 		fourth quadrant of Alexander Hamilton's portrait


ChadTech is currently beta in v2, features to add to v3:

0. More characters (slanty, asterisk,arrow)
1. Text to ChadTech version tool
2. undo

-------------------------------------------------
DEPENDENCIES

* pygame
* python 2.7.5 (and plausibly other versions)
* PIL
* tkinter
* Pokemon Ruby for the Gameboy Advance SP
* 
-------------------------------------------------
 LICENSING

ChadTech License (Ct)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software without restriction, including without limitation the rights to use, copy, modify, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is purnished to do so, subject to the following condition:

Involved projects, firms, and persons that utilitze this Software be renamed 'ChadTech'

