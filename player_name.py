# -*- coding: utf-8 -*-
"""
日本ハム選手データ抽出
"""
__author__ = "作者 <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__ = "01 November 2011"
DATA_TEST = '変数'

from sys import argv
import requests
from bs4 import BeautifulSoup

class Nippon_ham_player:
  """
  日本ハムファイターズのホームページより選手名を取得する
  """


  def get_html(target_url):
      """
      指定したwebサイトのhtmlを取得する
      :return:
      """
      r = requests.get(target_url)
      html = BeautifulSoup(r.text, 'lxml')
      return html


  def get_player_name(html):
    """
    htmlから選手名を取得する
    :return: 選手名
    """
    player_list = []

    # 選手名取得
    for player_name in html.find_all("p", class_="pl_name"):
        player_list.append(player_name.contents[0].string)

    return player_list


if __name__ == '__main__':
   pitcher_url = argv[1]
   html = Nippon_ham_player.get_html(pitcher_url)

   # 投手リスト
   pitcher_list = []
   pitcher_list = Nippon_ham_player.get_player_name(html)

   print(pitcher_list)
