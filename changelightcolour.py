import appdaemon.appapi as appapi

class ChangeLightColour(appapi.AppDaemon):

self.handle = self.listen_state(self.before_sunrise_cb, "light", new = "on", duration = 30, immediate = True, colour)