from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler


class CreateTagController:
    '''
        management for implementing business rules
    '''

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code=product_code)

        reponse_formatted = self.__format_response(path_from_tag=path_from_tag)

        return reponse_formatted

    def __create_tag(self, product_code: str) -> str:
        bardcode_handle = BarcodeHandler()

        path_from_tag = bardcode_handle.create_barcode(product_code=product_code)

        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:

        return {
            "data": {
                "type": "Tag Image",
                "amount": 1,
                "path": f'{path_from_tag}'
            } 
        }
    