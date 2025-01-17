
class SyntaxConfig(object):
    def __init__(self):
        # training configuration
        self.lr = 0.01
        self.batch_size = 200
        self.epoch = 200

        # dataset configuration
        self.dict_size = 20000
        self.pad_flag_index = 0     # padding在字典中的索引
        self.sos_flag_index = 1     # 开始标志在字典中的索引
        self.eos_flag_index = 2
        self.oov_flag_index = 3     # 超出字典词在字典中的索引

        # encoder configuration
        self.en_input_size = 100
        self.en_hidden_size = 100
        self.en_num_layers = 1
        self.en_bidirectional = True
        self.en_dropout_rate = 0

        # decoder configuration
        self.de_input_size = 100
        self.de_hidden_size = 100
        self.de_num_layers = 1
        self.de_bidirectional = False
        self.de_dropout_rate = 0
        self.de_out_class = 2

        # syntax_attn configuration
        self.syntax_input = 100
        self.syntax_output = 100
        self.linear_out = 100


