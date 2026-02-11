class InMemoryProductRepository(ProductRepository) :

    def __init__(self):
        self.__product : Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        self.__product[product.product_id] = product

    def get_by_id(self, product_id: str) -> Product:
        return self.__product.get(product_id)

    def update(self, product: Product):
        self.__product[product.product_id] = product

    def list_all_product(self) -> List[Product]:
        return list(self.__product.values())
