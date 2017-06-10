from pessoa import *

import hashlib

class Usuario(Pessoa):

	def __init__(self, nome, cpf, endereco, usuario, password=''):
		Pessoa.__init__(nome, cpf, endereco)			
		self.__usuario = usuario
		self.__password = self.__security_pass(password)

	# Getters

	def get_usuario(self):
		return self.__usuario

	
	def get_password(self):
		return self.__password

	# Setters

	def set_nome(self, nome=''):
		self.__nome = nome

	def set_usuario(self, usuario=''):
		self.__usuario = usuario

	def set_password(self, password):
		self.__password = self.__security_pass(password)

	def __security_pass(self, password):
		return hashlib.sha1(password).hexdigest()

