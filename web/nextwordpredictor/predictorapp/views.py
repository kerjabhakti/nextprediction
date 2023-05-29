from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
import os
from pickle import load
from predictormodel.model import NextWordModel
from keras import backend as K

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

MODEL_PATH = BASE_DIR + '/predictormodel/256-100.h5'
TOKENIZER_PATH = BASE_DIR + '/predictormodel/tokenizer.pkl'

INDO_MODEL_PATH = BASE_DIR + '/predictormodel/models/model6pre4.h5'
INDO_TOKENIZER_PATH = BASE_DIR + '/predictormodel/tokenizers/token6pre4.pkl'
INDO_PADDING_PATH = BASE_DIR + '/predictormodel/paddings/padding6pre4.pkl'

def load_language(tokenizer, m, overwrite_model=False):
	
	tokenizer_path = INDO_TOKENIZER_PATH
	model_path = INDO_MODEL_PATH
	print('Loading tokenizer...')
	tokenizer = load(open(tokenizer_path, 'rb'))
	tokenizer.oov_token = None
	print('\tDONE.')

print('Loading tokenizer...')
tokenizer = load(open(INDO_TOKENIZER_PATH, 'rb'))
tokenizer.oov_token = None
print('\tDONE.')

print('Loading padding...')
padding = load(open(INDO_PADDING_PATH, 'rb'))
print('\tDONE.')

model = NextWordModel()
model.load_model_tokenizer_and_padding(tokenizer, INDO_PADDING_PATH, INDO_MODEL_PATH)

max_sequence_len = padding

@api_view(['GET', 'POST'])
def predict(request):
	if request.method == 'POST':
		pretext = request.data['text']
		predicted_words = model.generate_seq(max_sequence_len, pretext, 1)
		return Response({"predicted_words": predicted_words})
	return Response({"text": "<TEXT HERE>"})

def index(request):
	return render(request,'index.html')