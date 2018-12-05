# PascalsTriangle
This is a sketch for the Processing, a flexible software sketchbook and a language for learning how to code within the context of the visual arts. This sketch produces a series of Pascal triangles to visualize the patterns that emerge as we color a set of the boxes according to simple rules. 

>"In mathematics, Pascal's triangle is a triangular array of the binomial coefficients. In much of the Western world, it is named after the French mathematician Blaise Pascal, although other mathematicians studied it centuries before him in India, Persia (Iran), China, Germany, and Italy.

>The rows of Pascal's triangle are conventionally enumerated starting with row n = 0 at the top (the 0th row). The entries in each row are numbered from the left beginning with k = 0 and are usually staggered relative to the numbers in the adjacent rows. The triangle may be constructed in the following manner: In row 0 (the topmost row), there is a unique nonzero entry 1. Each entry of each subsequent row is constructed by adding the number above and to the left with the number above and to the right, treating blank entries as 0. For example, the initial number in the first (or any other) row is 1 (the sum of 0 and 1), whereas the numbers 1 and 3 in the third row are added to produce the number 4 in the fourth row."

https://en.wikipedia.org/wiki/Pascal%27s_triangle

The trianlge has been shown to exhibit may strange behavours. For example, if we colour all the even number within the triangle white, and all the odd numb ers black, then what emerges is an approximation to the Sierpinski triangle. 

https://en.wikipedia.org/wiki/Sierpinski_triangle

We can see other patterns if, for example, we colour all the numbers that are divisible by 2, and another pattern if we colour the boxes divisible by 3, and so on. 

The program first constructs a Pascals triangle, then colours the boxes based on whether or not there are divisible by a number, then increments and creates the pattern for the next number. What emerges is a seriers of complex patterns that are unique for each number. Some of the patters anre exrremly intricate, while others are more regular.


The program has some varlables to allow for more or less rows. As the number of rows is increased, more of the pattern is revealed, but Skeep in mind that because of the way the Pascals Triangle is constructed, the numbers involved become very large very quickly. And although the arithmitic is relatively simple (is the number in this box divisible by n), the processing becomes slow when the numbers are very large. Fpr example, if we have 1000 rows, the maximium number which exists in the centre of the bottom row is 135144120472718284757807346812987637748076004223274143503696437553312714352761096949306241962251185082681303042510773052401104875025339958774947109849759237711832742131875866678081232039868943672182287080559748802285522492878143940257300497109713376183457928301568431301242214054648452931899910608160

When we let the program run for a while, we start to see more interesting behaviour. For example, the prime numbers all seem to produce a pattern of solid triangles, with the same number of rows as the prime number itself, before the triangles increase in size to the nex level.

For example, see the triable for mod 7. The smallest tirangles form a row of 7 inside the next biggest triangle. This next biggest also forms a row of 7 before the next size triangle appears. The pattern seems to hold for all the proime numbers, or at least the first few. Generating very large triangles becomes a probles as the sixe of the numbers involved makes processing very slow.

We also see some patterns that are very similiar, but the pattern appears to be drifting. 

It's not clear why these patterns emerge. 
