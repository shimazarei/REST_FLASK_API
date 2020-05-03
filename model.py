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
    "# this file contains different fucntions for different transactions to db.\n",
    "from flask import Flask\n",
    "from flask_sqlalchemy import SQLAlchemy\n",
    "import json\n",
    "from setting import app\n",
    "\n",
    "db = SQLAlchemy(app)\n",
    "\n",
    "class Data(db.Model):\n",
    "    tablename= 'node_tree'\n",
    "    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)\n",
    "    iNode = db.Column(db.Integer, primary_key=True)\n",
    "    level = db.Column(db.Integer, nullable=False)\n",
    "    iLeft = db.Column(db.Integer, nullable=False)\n",
    "    iRight = db.Column(db.Integer, nullable=False)\n",
    "    \n",
    "class Data_recive(db.Model):\n",
    "    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)\n",
    "    iNode = db.Column(db.Integer,db.ForeignKey('node_tree.iNode'), nullable=False)\n",
    "    Language = db.Column(db.String, nullable=False)\n",
    "    nodeName = db.Column(db.String, nullable=False)\n",
    "    \n",
    "def add_data(_iNode,_language,_nodeName):\n",
    "    new_data = Data_recive(iNode=_iNode, Language=_language, nodeName=_nodeName)\n",
    "    db.session.add(new_data)\n",
    "    db.session.commit()\n",
    "    \n",
    "def get_all_data(iNode):\n",
    "    return [Data.json(data) for data in Data.query.all()]\n",
    "\n",
    "\n",
    "#filter data by nodename\n",
    "def get_data_by_filter(_nodeName):\n",
    "    return Data_recive.query.filter_by(nodeName=_nodeName).first()\n",
    "  \n",
    "\n",
    "\n",
    "def delete_data(_iNode):\n",
    "    Data_recive.query.filter_by(iNode=_iNode).delete()\n",
    "    db.session.commit()\n",
    "\n",
    "\n",
    "def _repr_(self):\n",
    "    Data_object = {\n",
    "    'iNode':self.iNode,\n",
    "    'Language':self.Language,\n",
    "    'nodeName':self.nodeName ,\n",
    "    'num_of_page':self.num_of_page,\n",
    "    'page_size':self.page_size   \n",
    "    }\n",
    "    return json.dumps(Data_object)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\n"
   ]
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
