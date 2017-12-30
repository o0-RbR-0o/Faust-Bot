import random
import urllib
import requests
import html

from FaustBot.Communication.Connection import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype
from FaustBot.Modules.TitleObserver import TitleObserver

#template

class ShipmentObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return ['.shipment']

    @staticmethod
    def help():
        return '.shipment [NUMMER] liefert den Trackingstatus einer Paketsendung.'

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.shipment') == -1:
            return
        
