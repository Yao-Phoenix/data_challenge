# -*- coding: utf-8 -*-
import pandas as pd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        repo_name = item['repo_name']
        update_time = item['update_time']
        df_temp = pd.DataFrame([[repo_name, update_time]], columns=[
            'repo_name', 'update_time'])
        self.df = self.df.append(df_temp, ignore_index=True).sort_values(
                by='update_time', ascending=True)
        return item

    def open_spider(self, spider):
        self.df = pd.DataFrame(columns=['repo_name', 'update_time'])

    def close_spider(self, spider):
        self.df.to_csv('~/Code/shiyanlou_repo.csv', index=None)
