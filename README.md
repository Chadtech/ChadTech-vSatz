ChadTech
========

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

One character in ChadTech is saved in doc[] as a number, up to three digits long.

George:

But you said it was an image file?

Chad:

Yeah, it produces an image. When you save your document it produces an image of your text, and in the margins of the text, the text data (doc[]) is stored in the pixel color values. When you open an image in ChadTech, it reads the text data from the pixels.

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

The complicated features of google docs and word honestly get in the way far more than they help. I also think these programs are stuck in a paper nostalgia. I dont want long white pages with vector based fonts. Thats not how computers work. I want a black page, in the shape of my screen with a terminal-style font.

Also, do you mind if I abridge the hell out of this conversation and put it in the readme for ChadTech? I’ll make you say stuff like ‘Wow nice text editor Chad’.

George:

No I dont mind, and by the way, nice text editor Chad.

Chad:

Thanks George.

-------------------------------------------------

How to use ChadTech:

For the most part, if you press a key on your keyboard, the letter will show up in ChadTech, like any text editor. The features of ChadTech are controlled by hotkeys, which are listed below. All hotkeys should be pressed by holding down the first key, and then pressing the second, in that order and no other order.

ChadTech Commands:

	LCRTL then s                Save document

	LCTRL then o                Open document

	LSHIFT then Backspace       Backspace Ten Times

	LSHIFT then arrow key       move L/R ten times, or U/D five times

	LSHIFT then plus/equal key  Add superscript, or return to text if in subscript

	LSHIFT then minus key       Add subscript, or return to text if in superscript

FIRST ORDER LOGIC SYMBOLS:

	1 then e          Existential Quantifier

	1 then a          'For all'

	1 then i          Material Conditional, 'implies'

	1 then f          If, and only if. Symbol also means 'equivalent' and 'congruent' in other context

	1 then n          Negation

MODAL LOGIC SYMBOLS

	2 then p          Possible

	2 then n          Necessary

ChadTech is currently in v0.1, features to add:

1. Scrolling, if you go beyond the screen height the text shifts down, and if you save a document it saves one long image file.
2. 'exponential backspace/arrow keys', if you hold shift and backspace, each additional backspace is expontentially larger. For example you hold shift, press backspace, one character is removed, backspace again, 2, again, 4, again 8 etc.
3. Better response to 'Dummy Spaces' (spaces that you made not by pressing the space bar, but instead by say, pressing enter)
4. Better saving/opening of superscripts/subscripts. Right now its very buggy
5. More characters. Many characters are drawn and ready to implement into code.
6. Window that grows with your text, so small ChadTech documents are not mostly blackspace.
