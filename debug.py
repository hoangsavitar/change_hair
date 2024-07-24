
from hair_swap import HairFast, get_parser
model_args = get_parser()
hair_fast = HairFast(model_args.parse_args([]))

