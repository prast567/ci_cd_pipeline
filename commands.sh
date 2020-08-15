git clone git@github.com:prast567/ci_cd_pipeline.git
cd ci_cd_pipeline
git pull
make all
az webapp up -n flask-pred-app
