using FplAnalysis.ReturnClasses;
using RestSharp;

namespace FplAnalysis.Helper
{
    class Function
    {
        public static Model Initialise()
        {
            RestRequest request = FplApi.GetRequest();
            dynamic response = FplApi.ExecuteRequest(request, UriString.bootstrapStatic);
            return new Model(response);
        }
    }
}
