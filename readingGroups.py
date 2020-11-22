import json
import operator
from glob import glob
import matplotlib.pyplot as plt


class Reader:
    """
    this class declares readers that we will do our calculations on
    """
    def __init__(self, name, mobile_number, email, no_books, no_pages, category):
        """
        This is a constructor that assigns the values of the parameters to the attributes of the instance
        :param name:
        :param mobile_number:
        :param email:
        :param no_books:
        :param no_pages:
        :param category:
        """
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
        self.no_books = no_books
        self.no_pages = no_pages
        self.category = category

    def get_name(self):
        """
        An accessor
        :return: name of reader
        """
        return self.name

    def get_mobile_number(self):
        """
        An accessor
        :return: mobile number of the reader
        """
        return self.mobile_number

    def get_email(self):
        """
        An accessor
        :return: reader's E-mail
        """
        return self.email

    def get_no_books(self):
        """
        An accessor
        :return: number of books
        """
        return self.no_books

    def get_no_pages(self):
        """
        An accessor
        :return: number of pages per book
        """
        return self.no_pages

    def get_category(self):
        """
        An accessor
        :return: the category of the book
        """
        return self.category


class ReadingGroup:
    """
    This class groups readers in  a single instance
    """
    def __init__(self, name, max_num):
        self.name = name
        self.max_num = max_num
        self.readers = []

    def add_reader(self, reader):
        if len(self.readers) < self.max_num:
            self.readers.append(reader)
            return True
        return False

    def get_total_books(self):
        total_books = 0
        for reader in self.readers:
            total_books = total_books + reader.get_no_books()

        return "Total Number of books for {} is {} book".format(self.name, total_books)

    def get_total_pages(self):
        total_pages = 0
        for reader in self.readers:
            total_pages = total_pages + reader.get_no_pages()

        return "Total Number of pages for {} is {} page".format(self.name, total_pages)

    def get_book_categories(self):

        categories = {}
        for reader in self.readers:
            category = reader.get_category()

            for i in category:
                if i not in categories:
                    categories[i] = 1
                elif i in categories:
                    categories[i] = categories[i] + 1
        categories = sorted(categories.items(), key=operator.itemgetter(1), reverse=True)

        return categories

    def get_user_book_rank(self):
        book_rank = []
        for reader in self.readers:
            name = reader.get_name()
            books = reader.get_no_books()
            user = (name, books)
            book_rank.append(user)
        book_ranked = sorted(book_rank, key=lambda x: x[1], reverse=True)
        return book_ranked

    def get_user_page_rank(self):
        """
        :return: the page rank of the user
        """
        page_rank = []
        for reader in self.readers:
            name = reader.get_name()
            pages = reader.get_no_pages()
            user = (name, pages)
            page_rank.append(user)
        page_ranked = sorted(page_rank, key=lambda x: x[1], reverse=True)
        return page_ranked


group1 = ReadingGroup('Group1', 4)
group2 = ReadingGroup('Group2', 4)
group3 = ReadingGroup('Group3', 4)


def read_files():
    """
    opens the JSON file and deals with data in it
    :return:
    """
    for filename in glob('*.json'):
        with open(filename) as f:
            data = json.load(f)  # open the json file
            # do something with the data
            user_name = data['name']
            user_number = data['mobileNumber']
            user_email = data['email']
            category = []
            no_books = 0
            no_pages = 0
            # print("after opining file: ", user_name, user_number, user_email)

            for i in data['books']:
                no_books = no_books + 1

                for key in i:
                    if key == 'pages':
                        no_pages = no_pages + int(i[key])
                    elif key == 'category':
                        category.append(i[key])

        filename = Reader(user_name, user_number, user_email, no_books, no_pages, category)
        if group1.add_reader(filename):
            pass
        elif group2.add_reader(filename):
            pass
        elif group3.add_reader(filename):
            pass


def report(group_no):
    """

    :param group_no: takes group_no as an instance
    :return: report with all data and ranks of users and books
    """
    print("-------------------------------------------------------------")
    print(group_no.get_total_books())
    print(group_no.get_total_pages())
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    en = 1
    print("-------------------------------------------------------------")
    print('|{:^20}            |    {:^20} |'.format("Book Rank", "Page Rank"))
    print("-------------------------------------------------------------")
    for (i, j) in zip(group_no.get_user_book_rank(), group_no.get_user_page_rank()):
        b_rank = [i][0]
        p_rank = [j][0]

        line_new = '{:<20}  {:<4}  |   {:<20}  {:<5}'.format(b_rank[0], b_rank[1], p_rank[0], p_rank[1])
        print(en, "- ", line_new)
        en += 1
        x2.append(b_rank[0])
        y2.append(b_rank[1])
        x3.append(p_rank[0])
        y3.append(p_rank[1])
    print("-------------------------------------------------------------")
    print("Ranking of books categories mostly read by the group members: ")
    enu = 1

    for i in group_no.get_book_categories():
        cat = [i][0]
        if cat[1] < 2:
            continue
        else:
            print(enu, "- ", cat[0], cat[1])
            x1.append(cat[0])
            y1.append(cat[1])
        enu += 1
    # plt.plot(y1, x1, label="line 1")
    plot1 = plt.figure("Category Rank")
    plt.pie(y1, labels=x1, startangle=90, autopct='%1.1f%%')

    plot2 = plt.figure("Book Rank")
    plt.barh(x2, y2)

    plot3 = plt.figure("Page Rank")
    plt.barh(x2, y3)

    plt.show()

#__________Main()__________
group_no = ""
group_input = 1
start_input = input("Press 1 to read JSON files from current folder:")
while group_input >= 1:
    if start_input == "1":
        read_files()
        group_input = int(input("Press The Number of group to generate Report , 1, 2 or 3 OR press 0 to exit:"))
        if group_input == 0:
            break
        elif group_input == 1:
            group_no = eval("group" + str(group_input))
            report(group_no)
        elif group_input == 2:
            group_no = eval("group" + str(group_input))
            report(group_no)
        elif group_input == 3:
            group_no = eval("group" + str(group_input))
            report(group_no)

        else:
            print("Please enter the right group number.")
    else:break