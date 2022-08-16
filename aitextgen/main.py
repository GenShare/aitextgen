import aitextgen

## Trained model is mounted in S3, must contain config.json and pytorch_model.bin
#to_gpu may be false if in lambda
ai = aitextgen(model_folder="trained_model", to_gpu=True)

##min length: The minimum length of the generated text: if the text is shorter than this value after cleanup, aitextgen will generate another one.
##max_length: Number of tokens to generate (default 256, you can generate up to 1024 tokens with GPT-2 and 2048 with GPT Neo)
##temperature: The higher the temperature, the crazier the text (default 0.7, recommended to keep between 0.7 and 1.0)
##top_k: Limits the generated guesses to the top k guesses (default 0 which disables the behavior; if the generated output is super crazy, you may want to set top_k=40)
##top_p: Nucleus sampling: limits the generated guesses to a cumulative probability. (gets good results on a dataset with top_p=0.9)
## Worth looking into -- You can pass a batch_size to generate multiple samples in parallel, giving a massive speedup (in Colaboratory, set a maximum of 50 for batch_size to avoid going OOM).

texts = []
## Request for n generated texts
for i in range(0,n):
  texts.append(ai.generate_one(prompt={prompt},temperature={temp},max_length={max},min_length={min}))
  ## Probably want to implement a check here so ensure each element in array is unique
  
 return texts

