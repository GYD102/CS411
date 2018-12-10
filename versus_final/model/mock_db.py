class MockDB:

    @staticmethod
    def get_mock_senators():
        return {'Lamar Alexander': 'A000360', 'Kelly Ayotte': 'A000368', 'Tammy Baldwin': 'B001230',
                'John Barrasso': 'B001261', 'Max Baucus': 'B000243'}

    @staticmethod
    def get_mock_questions():
        return [
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum quis lectus faucibus, feugiat mi eu?',
            'Vestibulum dolor. Fusce dapibus at enim ac hendrerit. Etiam et cursus dui. Suspendisse at justo consequat?',
            'Vulputate sapien non, aliquam massa. Vivamus vitae nibh at nisi interdum tempus vel non odio. Nunc ligula eros?',
            'Dignissim quis cursus quis, fringilla lacinia leo. Cras eros ipsum, imperdiet eu sagittis euismod, cursus sed ipsum?',
            'Donec malesuada lacinia tortor, a consequat augue viverra non. Sed a leo convallis, malesuada nulla mollis?',
            'Blandit ante. Pellentesque at eleifend eros, et convallis felis. Maecenas euismod, nisi et sollicitudin aliquet?',
            'Nunc magna vestibulum velit, posuere pharetra risus ante non velit?'
        ]