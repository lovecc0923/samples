%% @author Administrator
%% @doc @todo Add description to test.


-module(test).

%% ====================================================================
%% API functions
%% ====================================================================
-export([m1/0]).



%% ====================================================================
%% Internal functions
%% ====================================================================

m1()->
%%  {ok, AuthSql}  = application:get_env(?MODULE, test),
%% AuthSql.
application:start(bson),
application:start(crypto),
application:start(mongodb),
{ok, Connection} = mongo:connect ([{database,<<"db0">>},{host,"114.119.6.150"},{port,27017}]),
Connection.