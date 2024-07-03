class Model:
    vault = {}

    @classmethod
    def query(cls, **kwargs):
        for k, v in kwargs.items():
            cls.vault[k] = v

    def __str__(self):
        if self.vault:
            st = ''
            for k, v in self.vault.items():
                st += f'{k} = {v}, '
            return f'Model: {st.rstrip(', ')}'
        return 'Model'


model = Model()
# model.query(id=1, fio='milan', old=35)

# print(model.vault)
# model.query(id1=1, fio2='milan', old2=35)

print(model.vault)
print(model)
