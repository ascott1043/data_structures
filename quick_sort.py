""" Two partitioning schemes:
(p) = Pivot
(s) = Start
(e) = End

Hoare: 
[11, 9, 29, 7, 2, 15, 28]

steps to sort:
1:  11p 9s  29  7   2   15  28e     #11 is pivot, start at 9
2:  11p 9   29s 7   2   15  28e     #9 < 11, so move onto 29
3:  11p 9   29s 7   2e  15  28      #end moves left until we get to a nbr < 11 (2)
4:  11p 9   2s  7   29e 15  28      #swap start (29) and end (2)
5.  11p 9   2   7s  29e 15  28      #move start right
6.  11p 9   2   7   29se 15 28      #7 < 11, so we move on again to 29
7.  11p 9   2   7e  29s 15  28      #move end left until it's < 11 (7)
8.  7   9   2   11p 29  15  28      #e and s pass eachother so swap pivot(7) with end (7)

#   11 is now in correct position
#   List is now partitioned into left [7,9,2] and right [29,15,28] 
#   Repeat process for each partition recursively

Lomuto:
(i) = Pivot Index
(I) = Index
[11, 9, 29, 7, 2, 15, 28]

steps to sort:
1. 11i  9   29  7   2   15  28p     #start with p as last element
2. 11   9i  29  7   2   15  28p     #move p index right bc i (11) < p (28)
3. 11   9   29i 7   2   15  28p     #move i right again to get to (29)
4. 11   9   29iI 7  2   15  28p     #

"""