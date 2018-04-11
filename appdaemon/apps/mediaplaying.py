# import appdaemon.plugins.hass.hassapi as hass
# # import appdaemon.appapi as appapi

# class MediaPlaying(hass.Hass):
# # class LightColour(appapi.AppDaemon):

#     def initialize(self):
#         self.listen_state(self.media_toggle, self.device_tracker.onkyo, new = "on", old = "off")

#     def media_toggle(self, entity, attribute, old, new, kwargs):
#         self.change_light()

#     def sun_change(self, kwargs):
#         self.change_light()

#     def change_light(self):
#         if self.get_state(self.light) == "on":
#             if self.now_is_between("sunset - 00:30:00", "sunrise - 00:30:00"):
#                 self.turn_on(self.args["activelight"], brightness = 200, kelvin = 2100, transition = 10)
#             else:
#                 self.turn_on(self.args["activelight"], brightness = 240, rgb_color = [255,222,173])