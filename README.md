# Booklet-Print-Order

Script for counting booklet printing page ordering. Allows you to make dual-sided booklets in various formats, using basic A4 paper.

## Usage

`Booklet.py [-h] [-e EMPTY_PAGE] [-m] pages {A4,A5,A6,A7,A8}`

- <u>**Positional arguments:**</u>
	- **pages** number of pages in book
	- **{A4,A5,A6,A7,A8}** booklet format and size

- <u>**Optional arguments:**</u>
	- **-h, --help** show this help message and exit
	- **-e EMPTY_PAGE, --empty_page EMPTY_PAGE** page number, which will be printed instead of blank pages in the end of booklet (default = 1)
	- **-m, --ms_office_fix** slice output to avoid limitation in MS Office products (255 chars) (default = false)

## Examples

### A5 booklet:

`Booklet 4 A5`

Output:<br>
**4,1,2,3**

![A5](https://user-images.githubusercontent.com/20092823/86597228-bd00be00-bf9b-11ea-8956-038ecf41f156.png)

------

### A6 booklet:

`Booklet 8 A6`

Output:<br>
**8,1,6,3,2,7,4,5**

![A6](https://user-images.githubusercontent.com/20092823/86597245-c12cdb80-bf9b-11ea-8d86-5951c2169fbc.png)

------

### A7 booklet:

`Booklet 16 A7`

Output:<br>
**16,1,14,3,12,5,10,7,4,13,2,15,8,9,6,11**

![A7](https://user-images.githubusercontent.com/20092823/86597247-c1c57200-bf9b-11ea-9a6f-5d74d87078f5.png)

------

### A8 booklet:

`Booklet 32 A8`

Output:<br>
**32,1,30,3,28,5,26,7,24,9,22,11,20,13,18,15,4,29,2,31,8,25,6,27,12,21,10,23,16,17,14,19**

![A8](https://user-images.githubusercontent.com/20092823/86597251-c1c57200-bf9b-11ea-9903-dbfbd8846395.png)

------

### Booklet with blank pages:

`Booklet 5 A6 -e 0`

Output:<br>
**0,1,0,3,2,0,4,5**

![Blank](https://user-images.githubusercontent.com/20092823/86597266-c558f900-bf9b-11ea-966d-f2278ab7ab8c.png)

------

### Simple booklet:

`Booklet 16 A5`

Output:<br>
**16,1,2,15,14,3,4,13,12,5,6,11,10,7,8,9**

![Simple](https://user-images.githubusercontent.com/20092823/86757672-98f8b780-c043-11ea-8944-2537e3d8ec54.png)

------

### Booklet splited into 2 parts:

`feature in progress`

Output:<br>
**feature in progress**

![Dual](https://user-images.githubusercontent.com/20092823/86757656-972ef400-c043-11ea-86c9-e5f2861a9273.png)

------

### Booklet splited into 4 parts:

`feature in progress`

Output:<br>
**feature in progress**

![Quad](https://user-images.githubusercontent.com/20092823/86757668-98602100-c043-11ea-9180-e63d22d51e45.png)

------

### Booklet with MS Office fix:

`Booklet 100 A5 -m`

Output:<br>
**100,1,2,99,98,3,4,97,96,5,6,95,94,7,8,93,92,9,10,91,90,11,12,89,88,13,14,87,86,15,16,85,84,17,18,83,82,19,20,81,80,21,22,79,78,23,24,77,76,25,26,75,74,27,28,73,72,29,30,71,70,31,32,69,68,33,34,67,66,35,36,65,64,37,38,63,62,39,40,61,60,41,42,59,58,43,44,57**
<br>
**56,45,46,55,54,47,48,53,52,49,50,51**

------
