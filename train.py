from aitextgen.aitextgen import aitextgen

ai = aitextgen(tf_gpt2="774M", to_gpu=True)
file_name = "input.csv"

ai.train(file_name,
         line_by_line=True,
         from_cache=False,
         num_steps=3000,
         generate_every=1000,
         save_every=1000,
         save_gdrive=False,
         learning_rate=1e-3,
         fp16=False,
         batch_size=1,
         )
