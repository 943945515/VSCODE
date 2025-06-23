import logging

# logging.debug("我是debug")
# logging.info("我是info")
# logging.warning("我是warning")
# logging.error("我是error")
# logging.critical("我是critical")
#logging默认的level就是warning,
#也就是说logging只会显示级别大于等于warning的日志信息



logging.basicConfig(filename='log.log',filemode='w',level=logging.NOTSET,format='%(levelname)s:%(asctime)s\t%(message)s')
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")