from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import file_parameters as fp


class FullCoinList:
    def __init__(self):
        self._download_coin_list()

    @staticmethod
    def _download_coin_list():
        try:
            html = urlopen('https://coinmarketcap.com/all/views/all/')
            soup = BeautifulSoup(html, 'html.parser')

            cols = []
            tr = soup.find('tr')
            ths = tr.findAll('th')
            for th in ths:
                cols.append(th.text.strip())

            df = pd.DataFrame(columns=cols)

            trs = soup.findAll('tr')
            for i_row, tr in enumerate(trs):
                tds = tr.findAll('td')
                for td, col in zip(tds, cols):
                    if col == 'Name':
                        df.at[i_row, col] = td.text.strip().split('\n')[1]
                    else:
                        df.at[i_row, col] = td.text.strip().split('\n')[0]

            df.to_csv(fp.fileSymbolListAll, index=False)
        except:
            pass
