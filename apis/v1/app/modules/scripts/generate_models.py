import io
import sys
from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator

def generate_model(host, user, password, database, outfile = "models.py"):
    engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')
    metadata = MetaData(bind=engine)
    metadata.reflect()
    outfile = io.open(outfile, 'w', encoding='utf-8') if outfile else sys.stdout
    generator = CodeGenerator(metadata)
    generator.render(outfile)

if __name__ == '__main__':
    print(sys.argv)


    # generate_model('localhost', 'postgres', 'engineer', 'dms1', 'models.py')
