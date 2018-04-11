# import appdaemon.plugins.hass.hassapi as hass

# class MediaPlaying(hass.Hass):

#     def initialize(self):
#         if "sensor" in self.args:
#             self.listen_state(self.state_change, sensor)

#     def state_change(self, entity, attribute, old, new, kwargs):
#         if new != "":
#             if