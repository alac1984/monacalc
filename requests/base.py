class BaseInvalidRequest:
    def __init__(self) -> None:
        self.errors: list = []

    def add_error(self, parameter: str, message: str) -> None:
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self) -> bool:
        return False

    def __repr__(self):
        return f"{type(self).__name__}(errors={self.errors})"


class BaseValidRequest:
    def __init__(self, **kwargs) -> None:
        self.filters = kwargs.get("filters", {})
        self.data = kwargs.get("data", {})

    def __bool__(self) -> bool:
        return True

    def __repr__(self):
        if self.filters:
            return f"{type(self).__name__}(filters={self.filters})"
        else:
            return f"{type(self).__name__}(data={self.data})"
