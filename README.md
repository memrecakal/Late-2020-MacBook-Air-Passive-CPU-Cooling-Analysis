# Late-2020 MacBook Air Passive CPU Cooling Analysis
Almost all electronic devices, especially computers, consist of processors, which are computing units. As the processors execute necessary operations, a considerable amount of heat occurs. Several solutions were developed to handle the heat effectively, such as forced convections via fans, passive cooling with fluids (heat exchangers), passive cooling with natural convection, etc.

A vast majority of the computers rely on passive and active cooling, putting front the active. Whether the system is a laptop or a desktop, fan(s) are employed to provide airflow and achieve cooling with forcing convection. As mentioned before, HX’s were also used in custom desktops for effective cooling. However, a relatively new and fascinating solution was presented by Apple Computers Inc. with the late-2020 model MacBook Air with M1 processors.

The Finite Volume Method is determined to be used in calculations with the help of the PIMPLE algorithm and chtMultiRegionFoam solver. The PIMPLE Algorithm combines PISO and SIMPLE and is used for transient cases. It has iterations instead of outer corrections in the SIMPLE algorithm for every time step, and once converged, it will move on to the next step until the solution is complete. The reason why chtMultiRegionFoam and PIMPLE are picked is that they are appropriate to use for steady/transient fluid flow and solid heat conduction along with the conjugate heat transfer between regions – just what we needed since we have both fluid and solid regions on which heat is transferred (convection and conduction are present simultaneously)

  

https://user-images.githubusercontent.com/42466646/151833227-3df90b31-2ebd-4b04-b4f3-42f6d93229dc.mp4



https://user-images.githubusercontent.com/42466646/151833342-f56d7598-0d4b-4b3b-9851-a55c5308e34c.mp4


  
 ![image](https://user-images.githubusercontent.com/42466646/151830537-4e8688ee-ce08-46d5-a231-998420a1a0e4.png)
