{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bc2b404b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Part 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2b3957e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Harry Potter and the Goblet of Fire, written by J.K Rowling\n",
      "Ivanhoe: A romance, written by Walter Scott\n"
     ]
    }
   ],
   "source": [
    "class Book:\n",
    "    def __init__(self, author=\"\", title=\"\"):\n",
    "        \"\"\"Initialize Book title w/ author & title.\"\"\"\n",
    "        self.author= author\n",
    "        self.title = title\n",
    "    def display(self):\n",
    "        \"\"\"Prints the book details as 'title, author'.\"\"\"\n",
    "        print(f\"{self.title}, written by {self.author}\")\n",
    "book1 = Book(\"J.K Rowling\", \"Harry Potter and the Goblet of Fire\")\n",
    "book2 = Book ( \"Walter Scott\", \"Ivanhoe: A romance\")\n",
    "book1.display()\n",
    "book2.display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "daa1dceb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
