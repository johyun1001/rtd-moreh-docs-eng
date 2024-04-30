
Moreh API document
===========================


Hardware
~~~~~~~~~~~~
moreh-smi에서 넘어오는 정보(SDA 및 token, 학습 process 정보)들을 다룹니다.


.. http:get:: /api/signal  
moreh-smi 가 설치된 노드들의 정보를 불러옵니다.


Parameters
-------------

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - Name
     - Description
   * - period
     - 시간 단위 입력 (ms, s, m, h, d, w, y)
   * - node 
     - 자세히 보고 싶은 노드의 IP를 입력합니다.
   * - param_name
     - 자세히 보고 싶은 정보를 입력합니다. (temp_gpu, temp_mem, util_gpu, util_mem, usage)


Responses
--------------

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - Code
     - Description
     - Schema
   * - 200
     - successful operation
     - PrometheusData []
   * - 600
     - syntax error
     - ErrorResponse
   * - 604
     - axios error
     - ErrorResponse


.. tabs::

   .. tab:: 200

      Prometheus reseponse. json array.
      
      **Media Type**: application/json

         **Schema**

         .. code-block:: shell

            [PrometheusData{
            metric	{...}
            value	[...]
            }]

         **Example Value** 

         .. code-block:: shell

            [
               {
                  "metric": {
                     "__name__": "gpu_info",
                     "device_index": "0",
                     "gpu_type": "AMD",
                     "instance": "backnode01",
                     "job": "moreh_exporter",
                     "param_name": "temp_gpu, temp_mem, util_gpu, util_mem, usage"
                  },
                  "value": [
                     0,
                     "string"
                  ]
               }
            ]

   .. tab:: 600

      syntax error.

      **Media Type**: application/json

      
      **Schema**

      .. code-block:: shell

         {
         code	integer
         example: 10061
         에러 코드

         details	string
         example: SyntaxError. check parameters type.
         에러 설명

         }

      **Example Value** 

      .. code-block:: shell

         {
         "code": 10061,
         "details": "SyntaxError. check parameters type."
         }

   .. tab:: 604

      axios error.

      **Media Type**: application/json

      **Schema**

      .. code-block:: shell

         string
         prometheus error response

      **Example Value** 

      .. code-block:: shell

         "string"







Check
~~~~~~~~~~~~

API 와 DB 및 gRPC 상태를 확인합니다. API가 에러일 경우 모두 에러로 표시됩니다.

.. http:get:: /api/check

Parameters
-------------

.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - Name
     - Description
     - Schema
   * - type
     - Node IP를 지정할 경우, 해당 노드의 정보만 불러옵니다. 이 값이 정해져있지 않으면 모든 노드의 정보를 불러옵니다. (Available values : api, ipmi, db, grpc 중 선택 (default = api))
     - String
   * - node 
     - 자세히 보고 싶은 노드의 IP를 입력합니다.
     - String
   * - param_name
     - 자세히 보고 싶은 정보를 입력합니다. (temp_gpu, temp_mem, util_gpu, util_mem, usage)
     - String

Responses
--------------


.. list-table:: 
   :widths: 20 60 20
   :header-rows: 1

   * - Code
     - Description
     - Schema
   * - 200
     - successful operation
     - string (ex. OK)
   * - 600
     - syntax error
     - ErrorResponse









Backend
~~~~~~~~~~~~

moreh-smi에서 넘어오는 정보들을 다루고 Backend 정보를 모두 불러옵니다.

.. http:get:: /api/backend


Parameters
-------------

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
     - Schema
   * - type
     - Node IP를 지정할 경우, 해당 노드의 정보만 불러옵니다. 이 값이 정해져있지 않으면 모든 노드의 정보를 불러옵니다. (Available values : api, ipmi, db, grpc 중 선택 (default = api))
     - String
   * - node 
     - 자세히 보고 싶은 노드의 IP를 입력합니다.
     - String
   * - param_name
     - 자세히 보고 싶은 정보를 입력합니다. (temp_gpu, temp_mem, util_gpu, util_mem, usage)
     - String

Responses
--------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Code
     - Description
     - Schema
   * - 200
     - successful operation
     - string (ex. OK)
   * - 600
     - syntax error
     - ErrorResponse


SDA Model
~~~~~~~~~~~~

At this point optional parameters `cannot be generated from code`_.
However, some projects will manually do it, like so:

This example comes from `django-payments module docs`_.

.. class:: payments.dotpay.DotpayProvider(seller_id, pin[, channel=0[, lock=False], lang='pl'])

   This backend implements payments using a popular Polish gateway, `Dotpay.pl <http://www.dotpay.pl>`_.

   Due to API limitations there is no support for transferring purchased items.


   :param seller_id: Seller ID assigned by Dotpay
   :param pin: PIN assigned by Dotpay
   :param channel: Default payment channel (consult reference guide)
   :param lang: UI language
   :param lock: Whether to disable channels other than the default selected above

.. _cannot be generated from code: https://groups.google.com/forum/#!topic/sphinx-users/_qfsVT5Vxpw
.. _django-payments module docs: http://django-payments.readthedocs.org/en/latest/modules.html#payments.authorizenet.AuthorizeNetProvide


SDA
~~~~~~~~~~~~

.. data:: Data_item_1
          Data_item_2
          Data_item_3

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce congue elit eu hendrerit mattis.

Some data link :data:`Data_item_1`.



Some of the API requests (especially the ones that are read-only GET
requests) do not require any authentication.  The other ones, that modify data
into the database, require broker authentication via API key.  Additionally,
owner tokens are issued to facilitate multiple actor roles upon object creation.

API keys
~~~~~~~~~~~~

Basic Authenication
~~~~~~~~~~~~~~~~~~~
API key is username to use with Basic Authentication scheme (see :rfc:`2617#section-2`).

Bearer Authenication
~~~~~~~~~~~~~~~~~~~~
API key is token to use with Bearer Authentication scheme

Owner tokens
~~~~~~~~~~~~

Getting token
~~~~~~~~~~~~~

The token is issued when object is created in the database:

.. http:example:: tendering/belowthreshold/http/tutorial/create-tender-procuringEntity.http
   :code:

You can see the `access` with `token` in response.  Its value can be used to
modify objects further under "Owner role".  

Using token
~~~~~~~~~~~

You can pass access token in the following ways:

1) `acc_token` URL query string parameter
2) `X-Access-Token` HTTP request header
3) `access.token` in the body of POST/PUT/PATCH request

See the example of the action with token passed as URL query string:

.. http:example:: tendering/belowthreshold/http/tutorial/patch-items-value-periods.http
   :code:



.. tabs::

   .. group-tab:: Linux

      Linux tab content - tab set 2

   .. group-tab:: Mac OSX

      Mac OSX tab content - tab set 2

   .. group-tab:: Windows

      Windows tab content - tab set 2






The tab selection in these groups is synchronised, so selecting the 'Linux' tab of one tab set will open the 'Linux' tab contents in all tab sets on the current page.

If permitted by the user's browser, the last selected group tab will be remembered when changing page in the current session. As such, if any tabsets on the next page contain a tab with the same label it will be selected.

Code Tabs
~~~~~~~~~~~~

A common use of group tabs is to show code examples in multiple programming languages. The `code-tab` directive creates a group tab and treats the tab content as a `code-block`.

The first argument to a `code-tab` is the name of the language to use for code highlighting, while the optional second argument is a custom label for the tab. By default, the tab is labelled using the lexer name. The tab label is used to group tabs, so the same custom label should be used to group related tabs.

.. code-block:: RST

   .. tabs::

      .. code-tab:: c

            C Main Function

      .. code-tab:: c++

            C++ Main Function

      .. code-tab:: py

            Python Main Function

      .. code-tab:: java

            Java Main Function

      .. code-tab:: julia

            Julia Main Function

      .. code-tab:: fortran

            Fortran Main Function

      .. code-tab:: r R

            R Main Function

   .. tabs::

      .. code-tab:: c

            int main(const int argc, const char **argv) {
            return 0;
            }

      .. code-tab:: c++

            int main(const int argc, const char **argv) {
            return 0;
            }

      .. code-tab:: py

            def main():
               return

      .. code-tab:: java

            class Main {
               public static void main(String[] args) {
               }
            }

      .. code-tab:: julia

            function main()
            end

      .. code-tab:: fortran

            PROGRAM main
            END PROGRAM main

      .. code-tab:: r R

            main <- function() {
               return(0)
            }


.. tabs::

   .. code-tab:: c

         C Main Function

   .. code-tab:: c++

         C++ Main Function

   .. code-tab:: py

         Python Main Function

   .. code-tab:: java

         Java Main Function

   .. code-tab:: julia

         Julia Main Function

   .. code-tab:: fortran

         Fortran Main Function

   .. code-tab:: r R

         R Main Function


Code tabs support highlighting using `custom syntax highlighters <https://pygments.org/docs/lexerdevelopment/>`_ that have been loaded in the sphinx configuration. To use custom lexers, pass the lexers alias as the first argument of `code-tab`.


The dropdown directive combines a Bootstrap card with the HTML details tag to create a collapsible drop-down panel.

.. dropdown:: Click on me to see my content!

    I'm the content which can be anything:

    .. link-button:: https://example.com
        :text: Like a Button
        :classes: btn-primary
.. dropdown:: Click on me to see my content!

    I'm the content which can be anything:

    .. link-button:: https://example.com
        :text: Like a Button
        :classes: btn-primary






.. cpp:type:: MyType

   Some type

.. cpp:function:: const MyType Foo(const MyType bar)

   Some function type thing

.. cpp:class:: template<typename T, std::size_t N> std::array

   Some cpp class

.. cpp:member:: float Sphinx::version

   The description of Sphinx::version.

.. cpp:var:: int version

   The description of version.

.. cpp:type:: std::vector<int> List

   The description of List type.

.. cpp:enum:: MyEnum

   An unscoped enum.

   .. cpp:enumerator:: A

.. cpp:enum-class:: MyScopedEnum

   A scoped enum.

   .. cpp:enumerator:: B

.. cpp:enum-struct:: protected MyScopedVisibilityEnum : std::underlying_type<MySpecificEnum>::type

   A scoped enum with non-default visibility, and with a specified underlying type.

   .. cpp:enumerator:: B






.. Copied from sphinx-doc/sphinx/tests/roots

.. js:module:: module_a.submodule

* Link to :js:class:`ModTopLevel`

.. js:class:: ModTopLevel

    * Link to :js:meth:`mod_child_1`
    * Link to :js:meth:`ModTopLevel.mod_child_1`

.. js:method:: ModTopLevel.mod_child_1

    * Link to :js:meth:`mod_child_2`

.. js:method:: ModTopLevel.mod_child_2

    * Link to :js:meth:`module_a.submodule.ModTopLevel.mod_child_1`

.. js:module:: module_b.submodule

* Link to :js:class:`ModTopLevel`

.. js:class:: ModNested

    .. js:method:: nested_child_1

        * Link to :js:meth:`nested_child_2`

    .. js:method:: nested_child_2

        * Link to :js:meth:`nested_child_1`

Copyright © 2022 Moreh Corporation