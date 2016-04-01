import os

import riffle

logOutput = os.environ.get("LOG_HEADER", "default")

class ExampleSession(riffle.Domain):
    def onJoin(self):
        self.register("echo", self.echo)

    @riffle.want(str)
    def echo(self, msg):
        print("{}: {}".format(logOutput, msg))
        return msg


if __name__ == "__main__":
    riffle.SetFabric(os.environ['WS_URL'])
    
    riffle.SetLogLevelInfo()
    domain = os.environ['DOMAIN']
    ExampleSession(domain).join()
