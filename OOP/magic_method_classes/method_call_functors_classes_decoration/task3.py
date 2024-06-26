class ImageFileAcceptor:
    # acceptor = ImageFileAcceptor(extensions)
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, name, *args, **kwargs):
        start = name.rfind('.')
        ext = '' if start == -1 else name[start + 1:]
        return ext in self.extensions


if __name__ == '__main__':
    filenames = ['b.oat.jpg', 'dog.jpg', 'c.at.png', 'text.txt', 'python.doc', 'eq.png', 'data.html', 'dack.xls']
    acceptor = ImageFileAcceptor(['jpg', 'jpeg', 'bmp'])
    image_filenames = filter(acceptor, filenames)
    print(list(image_filenames))
