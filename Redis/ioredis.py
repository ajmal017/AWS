var Redis = require('ioredis');
var redis = new Redis();



redis.lrange('test',0,-1, function (err, result) {
    if (err) {
      console.error(err);
    } else {
      console.log(result);
    }
  });

redis.quit()
