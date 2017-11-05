import appdaemon.appapi as appapi

class LightColour(appapi.AppDaemon):

    def initialize(self):
        self.listen_state(self.lights_on, self.args["activelight"], new = "on", old = "off")

    def lights_on(self, entity, attribute, old, new, kwargs):
        if self.now_is_between("sunset - 00:30:00", "sunrise - 00:30:00"):
            self.turn_on(self.args["activelight"], brightness = 200, color_name = "sandy brown" transition = 30)
        else:
            self.turn_on(self.args["activelight"], brightness = 240, rgb_color = [255,222,173])