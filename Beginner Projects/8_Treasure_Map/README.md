## Treasure Map

This is to try and simulate the coordinates on a real map. 

![](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg)

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

![](https://cdn.fs.teachablecdn.com/PfApnWnTam1pLUeKbUWZ)

First your program must take the user input and convert it to a usable format. 

Next, you need to use it to update your nested list with an "x". 

# Example Input 1

column 2, row 3 would be entered as:

```
23
```

# Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```

# Example Input 2

column 3, row 1 would be entered as:

```
31
```

# Example Output 2

```
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```


>> python treasure_map.py

e.g. When you run this file, this is what should happen: 

![](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)

