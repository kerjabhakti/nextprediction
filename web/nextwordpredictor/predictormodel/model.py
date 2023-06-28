from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences

class NextWordModel(object):
	"""docstring for NextWordModel"""
	def __init__(self):
		super(NextWordModel, self).__init__()
	
	def load_model_tokenizer_and_padding(self, tokenizer, padding, model_path):
		self.tokenizer = tokenizer
		print('Loading model...')
		self.padding = padding
		print('Loading model...')
		self.model = load_model(model_path, compile=False)
		self.model.make_predict_function()
		print('Model Loaded!')

	def generate_seq(self, max_sequence_len, seed_text, n_words):
		result = list()
		in_text = seed_text
		# generate a fixed number of words
			# for _ in range(n_words):
		# encode the text as integer
		print(seed_text)

		next_words = 1

		for _ in range(next_words):
			token_list = self.tokenizer.texts_to_sequences([in_text])[0]
			# truncate sequences to a fixed length
			# token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
			token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
			# predict probabilities for each word
			# yhat = self.model.predict_classes(encoded, verbose=0)
			predicted_l = list(tuple(enumerate(self.model.predict(token_list)[0])))
			top_2 = sorted(predicted_l, key=lambda x: x[1], reverse=True)[:2]
			print(top_2)
			# map predicted word index to word
			predicted_words = []
			for i, word in enumerate(top_2):
				for w in list(self.tokenizer.word_index.items()):
					if w[1] == word[0]:
						predicted_words.append({'word': w[0], 'probability': word[1]})
		return predicted_words 