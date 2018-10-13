#!/usr/bin/python

import sets

class Error( Exception ):
	"""Basic class for exceptions in this module."""

	pass

class IllegalTranslationFormatError( Error ):
	"""Exception for illegal translation formats."""

	pass

	
class Translator:
	"""Translator class for hackerize module."""

	def __init__( self ):
		"""Object initialization."""

		self._transMap = {}

		self._fileType = "text/plain"

		self._xmlParametersForTranslate = sets.Set()

	def setFileType( self , type ):
		"""Set file type."""

		self._fileType = type
	
	def getFileType( self ):
		"""Returns file type."""

		return self._fileType

	def setXMLParamatersForTranslate( self , parameters ):
		"""Sets XML tag parameters, which will be also translated."""

		self._xmlParametersForTranslate = parameters
	
	def addTranslation( self , translation ):
		"""Adds signle translation pair.

		translation is two-element tuple containg
		char and destination text."""

		if type( translation ) != type(()) or len( translation ) != 2:
			raise IllegalTranslationFormatError

		self._transMap[ translation[0] ] = translation[1]

	def addTranslations( self , translations ):
		"""Adds translation pairs dictionary.

		translation is two-element tuple containg
		char and destination text."""

		if type( translations ) != type({}):
			raise IllegalTranslationFormatError

		for translation in translations:
			self.addTranslation( translation )

	def clearTranslations( self ):
		"""Clears all translations."""

		self._transMap = {}

	def _translate( self , string ):
		"""Translates raw-string with setted translations.

		File type checking isn't performed."""

		return "".join( [ self._transMap.get( x , x ) for x in string ] )
		
	def translate( self , string ):
		"""Translates string with setted translations.
		
		File type checking is performed."""

		if self._fileType == "text/plain":
			return self._translate( string )

		
