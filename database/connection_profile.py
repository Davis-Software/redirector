class ConnectionProfile:
    def __init__(self, host: str, port: int, database: str, username: str, password: str, sql_type: str):
        self.mysql_host = host
        self.mysql_port = port
        self.mysql_database = database
        self.mysql_username = username
        self.mysql_password = password
        self.sql_type = sql_type
        
    @property
    def connection_uri(self):
        if self.sql_type == "sqlite":
            uri_elements = [
                'sqlite:///',
                self.mysql_database
            ]
        elif self.sql_type == "mysql":
            uri_elements = [
                'mysql://',
                self.mysql_username,
                ':',
                self.mysql_password,
                '@',
                self.mysql_host,
                ':',
                self.mysql_port,
                '/',
                self.mysql_database
            ]
        else:
            raise TypeError("No such SQLType", self.sql_type)
        
        return ''.join(uri_elements)
