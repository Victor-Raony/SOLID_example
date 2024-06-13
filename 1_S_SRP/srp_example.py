#Primeiro principio de SOLID: Principio de responsabilidade unica

class Process:
  def handler(self, username: str, password: str) -> None:
    if self.__verify_input_data(username, password):
      self.__verify_input_in_database(username)
      self.__insert_new_user(username, password)
    else:
      self.__raise_error('Dados invalidos')
    
  def __verify_input_data(self, username: str, password: str) -> bool:
    return isinstance(username, str and isinstance(password, str))
  
  def __verify_input_in_database(self, username: str) -> None:
    print('Acessando a base de dados...')
    print('Verificando se o usuário existe...')
    
  def __insert_new_user(self, username: str, password: str) -> None:
    print('Cadastrado de usuario realizado com sucesso!')
    
  def __raise_error(self, message: str) -> Exception:
    raise Exception(message)