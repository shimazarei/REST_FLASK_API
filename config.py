{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# I use this script for creating databse and also reading sql files which are generated for creating tablea\n",
    "# and saving data into tables.\n",
    "import mysql\n",
    "import mysql.connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<mysql.connector.connection_cext.CMySQLConnection object at 0x10effafd0>\n"
     ]
    }
   ],
   "source": [
    "mydb = mysql.connector.connect(\n",
    "  host=\"localhost\",\n",
    "  user=\"root\",\n",
    "  passwd=\"shima1983\"\n",
    ")\n",
    "print(mydb)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#cur = mydb.cursor()\n",
    "#cur.execute(\n",
    "#\"CREATE DATABASE DB1 \"\n",
    "#)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mydb = mysql.connector.connect(\n",
    "  host=\"localhost\",\n",
    "  user=\"root\",\n",
    "  passwd=\"shima1983\",\n",
    "  database=\"DB1\"  \n",
    ")\n",
    "curs= mydb.cursor()\n",
    "\n",
    "def executeScriptsFromFile(filename):\n",
    "    # Open and read the file as a single buffer\n",
    "    fd = open(filename, 'r')\n",
    "    sqlFile = fd.read()\n",
    "    fd.close()\n",
    "\n",
    "    # all SQL commands (split on ';')\n",
    "    sqlCommands = sqlFile.split(';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "executeScriptsFromFile('./table.sql')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('table.sql', 'r')\n",
    "query = \" \".join(f.readlines())\n",
    "for _ in curs.execute(query, multi=True): pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mydb = mysql.connector.connect(\n",
    "  host=\"localhost\",\n",
    "  user=\"root\",\n",
    "  passwd=\"shima1983\",\n",
    "  database=\"DB1\"  \n",
    ")\n",
    "curs= mydb.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "curs.execute(\"SHOW TABLES\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('node_tree',)\n",
      "('node_tree_name',)\n"
     ]
    }
   ],
   "source": [
    "for table in curs:\n",
    "    print(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mydb = mysql.connector.connect(\n",
    "  host=\"localhost\",\n",
    "  user=\"root\",\n",
    "  passwd=\"shima1983\",\n",
    "  database=\"DB1\"  \n",
    ")\n",
    "curs= mydb.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "executeScriptsFromFile('./data.sql')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('data.sql', 'r')\n",
    "query = \" \".join(f.readlines())\n",
    "for _ in curs.execute(query, multi=True): pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mydb = mysql.connector.connect(\n",
    "  host=\"localhost\",\n",
    "  user=\"root\",\n",
    "  passwd=\"shima1983\",\n",
    "  database=\"DB1\"  \n",
    ")\n",
    "curs= mydb.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "curs.execute(\"SELECT * FROM node_tree_name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
