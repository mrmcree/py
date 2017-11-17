# Scrapy settings for example project
# coding=utf-8
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
# redis的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停 ，redis记录不丢失
SCHEDULER_PERSIST = True
# 默认的scrapy-redis请求集合
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# x先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
# 写入redis数据库的管道
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'
# REDIS_HOST=''
# REDIS_PORT=''
# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1
