from abc import ABCMeta, abstractmethod


class CommonMailService(metaclass=ABCMeta):

    @abstractmethod
    def send_mail(self, email):
        pass
