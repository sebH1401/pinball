from pinball.Vector import Vector


class Utils:
    @staticmethod
    def get_cord_list(elements: list[Vector]) -> list[float]:
        cord_list = []
        for element in elements:
            cord_list.append(element.x)
            cord_list.append(element.y)
        return cord_list
