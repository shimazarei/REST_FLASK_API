{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/shimazarei/anaconda3/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:814: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to \"sqlite:///:memory:\".\n",
      "  'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '\n",
      "/Users/shimazarei/anaconda3/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.\n",
      "  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '\n"
     ]
    }
   ],
   "source": [
    "# This file contains URI to my database to connect to my db and tables.\n",
    "from flask import Flask\n",
    "from flask_sqlalchemy import SQLAlchemy\n",
    "app = Flask(__name__)\n",
    "\n",
    "app.config['SQLALCHAMEY_DATBASE_URI'] = 'mysql://username:password@localhost/DB1'\n",
    "db = SQLAlchemy(app)\n"
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
