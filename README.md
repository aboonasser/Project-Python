
The project is programmed with python programming langage,
python version:3.8
libraries used:
	- json
	- operator
	- glob
	- matplotlib( must be downloaded )

1- the program gets input data from json files with spacific structure:

{
    "name": "john duo",
    "mobileNumber": "0516126515000",
    "email": "john@gmail.com",

    "books": [
        {
            "bookTitle": "vampire diaries",
            "pages": 764 ,
            "category":"super natural"
        },
        {
            "bookTitle": "the fall",
            "pages": 987 ,
            "category":"horror"
        },
        {
            "bookTitle": "the night eternal",
            "pages": 155 ,
            "category":"super natural"
        },
        {
            "bookTitle": "the convoluted universe",
            "pages": 966 ,
            "category":"astrology"
        },
        {
            "bookTitle": "rangers",
            "pages": 317 ,
            "category":"documentary"
        }
    ]
}

2- the json files must be at the same folder as the program script (readingGroups.py)
3- the program is set to 3 groups for 20 reader for each, two test the 3 groups are working lower the limit of each group to 4 to match the 12 exicting json files 
   or increase the number of json files in folder 
