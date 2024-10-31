import argparse

# Function for parsing arguments
def arg_parse():

    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Model arguments
    parser.add_argument('-m',   '--model',             type=str,   default = 'LSTM',         help="Which model to use")

    # LSTM model arguments
    parser.add_argument('-hs',  '--hidden_dim',        type=int,   default = 64,             help="Size of the models hidden layer")
    parser.add_argument('-es',  '--embedding_dim',     type=int,   default = 768,            help="Size of the embedding space")
    parser.add_argument('-nl',  '--number_of_layers',  type=int,   default = 2,              help="Number of layers in the model")

    # Training arguments
    parser.add_argument('-e',   '--epochs',            type=int,   default = 30,             help="Number of epochs in training")
    parser.add_argument('-lr',  '--learning_rate',     type=float, default = 0.00001,        help="Learning rate in training")

    # Data arguments
    parser.add_argument('-sl',  '--sequence_length',   type=int,   default = 6,              help="Length of the sequences that will be extracted")
    parser.add_argument('-bs',  '--batch_size',        type=int,   default = 256,            help="Batch size")

    # Parse the arguments
    return parser.parse_args()